import sys
import os
from dotenv import load_dotenv
import openpyxl
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
        except KeyError:
            print(f"Error: Sheet '{'TenderPreparation'}' not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


    # EGP Credentials
    website_url = "https://www.eprocure.gov.bd/"
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("PASSWORD")
    

    pkg_no, pkg_name, location, budget, estimated_cost, quantity, unit = str(read_cell_value('G15')), str(read_cell_value('G16')), str(read_cell_value('G17')), str(read_cell_value('G18')), str(read_cell_value('G19')), str(read_cell_value('G21')), str(read_cell_value('G22'))

    financial_year, budget_type, approval_status, app_id, tender_type = str(read_cell_value('G26')), str(read_cell_value('G27')), str(read_cell_value('G28')), str(read_cell_value('G29')), str(read_cell_value('G32'))
    procur_nature, emrgency, app_cost, approv_authority, procure_type = str(read_cell_value('G33')), str(read_cell_value('G34')), str(read_cell_value('G35')), str(read_cell_value('G39')), str(read_cell_value('G40'))
    procure_method, exp_ift_dt, submsn_duration, opening_duration, eval_submn_duration = str(read_cell_value('G41')), str(read_cell_value('G44').strftime("%d/%m/%Y")), str(read_cell_value('G45')), str(read_cell_value('G46')), str(read_cell_value('G47'))
    contract_aproval_duration, noa_duration, contr_sign_durataion, contr_comp_duration = str(read_cell_value('G48')), str(read_cell_value('G49')), str(read_cell_value('G50')), str(read_cell_value('G51'))

    # Create an instance of EgpTenderPlotter
    tender_plotter = EgpTenderPlotter(website_url, email_address, email_password)


    print(f"package information of {pkg_no} loaded.")

    package_info = PackageDetails(pkg_no, pkg_name, location, budget, estimated_cost, quantity, unit)
    package_app = AppPackage(financial_year, budget_type, approval_status, app_id, tender_type, 
                 procur_nature, emrgency, app_cost, approv_authority, procure_type, 
                 procure_method, exp_ift_dt, submsn_duration, opening_duration, eval_submn_duration,
                 contract_aproval_duration, noa_duration, contr_sign_durataion, contr_comp_duration)

    try:
        # If the website loaded then do other things.
        if tender_plotter.load_website():

            # Log in to e-GP Portal
            if tender_plotter.login():
                tender_plotter.close_popup()
                tender_plotter.select_my_app_submenu()
                tender_plotter.select_app(package_app.financial_year, package_app.budget_type, package_app.approval_status, package_app.app_id)
                
                print(f"Adding {package_info.pkg_no} to the APP ID = {package_app.app_id}.")
                tender_plotter.add_project_to_app(package_info, package_app)
                
                

                print("Do other things.")
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

