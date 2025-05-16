import sys
import openpyxl
import os
from dotenv import load_dotenv
from egp_tender_plotter import AppPackage, EgpTenderPlotter, PackageDetails


try:
    if len(sys.argv) < 2:
        raise ValueError("Please provide a parameter.")
    
    parameter = sys.argv[1]


    def read_cell_value(cell_address):
        try:
            workbook = openpyxl.load_workbook(parameter, data_only=True)
            sheet = workbook['TenderPreparation']
            cell_value = sheet[cell_address].value
            workbook.close()

            return cell_value
        except FileNotFoundError:
            print("Error: File not found.")
            return False
        except KeyError:
            print(f"Error: Sheet '{'TenderPreparation'}' not found.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return False




    def write_te_excel(input_cell_address_dict):
        try:
            if input_cell_address_dict:
                workbook = openpyxl.load_workbook()
                sheet = workbook['TenderPreparation']
                for key, value in input_cell_address_dict.items():
                    sheet[key] = value
                workbook.close()
                return True
            else:
                return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False
        except KeyError:
            print(f"Error: Sheet '{'TenderPreparation'}' not found.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return False



    # EGP Credentials
    website_url = "https://www.eprocure.gov.bd/"
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("PASSWORD")

    tender_id  = str(read_cell_value('G57'))
    tender_plotter = EgpTenderPlotter(website_url, email_address, email_password, "headless")


    print(f"package information of {tender_id} loaded.")

   
    try:
        if tender_plotter.load_website():
            payment_details_dict = {}

            # Log in to e-GP Portal
            if tender_plotter.login():
                tender_plotter.close_popup()
                tender_plotter.select_my_tender_submenu(True)
                if tender_plotter.select_a_package_from_processing_tab(tender_id):
                    print(f"the {tender_id} is found in Processing Tab.")
                    payment_details_dict = tender_plotter.get_performance_secrity_payment_details(tender_id)

                elif tender_plotter.select_a_package_from_archived_tab(tender_id):
                    print(f"the {tender_id} is found in Archived Tab.")
                    payment_details_dict = tender_plotter.get_performance_secrity_payment_details(tender_id)

                else:
                    print(f"{tender_id} not found in My Tender Page")

                print (payment_details_dict)
                
            else:
                print("Unable to login to the EGP System.")
        else:
            print("Unable to load the e-GP website.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        input("\nPress Enter to close the browser...")
        tender_plotter.quit()


except ValueError as ve:
    print("Error:", ve)
    print("Usage: python script_name.py <parameter>")
    sys.exit(1)  # Exit with error code 1 if no parameter is provided

