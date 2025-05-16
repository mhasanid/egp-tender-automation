import sys
import openpyxl
import os
from dotenv import load_dotenv
from egp_tender_plotter import AppPackage, EgpTenderPlotter, PackageDetails, TenderNotice


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
        except KeyError:
            print(f"Error: Sheet '{'TenderPreparation'}' not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


    # EGP Credentials
    website_url = "https://www.eprocure.gov.bd/"
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("PASSWORD")


    # Create an instance of EgpTenderPlotter
    tender_plotter = EgpTenderPlotter(website_url, email_address, email_password)

    tender_id  = str(read_cell_value('G57'))

    try:
        # If the website loaded then do other things.
        if tender_plotter.load_website():

            # Log in to e-GP Portal
            if tender_plotter.login():
                tender_plotter.update_info_later()
                tender_plotter.select_my_tender_submenu(False)
                tender_plotter.select_a_package_from_processing_tab(tender_id)
                tender_plotter.download_documents_for_evaluation(tender_id)
                
                
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