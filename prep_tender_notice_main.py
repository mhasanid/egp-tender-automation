import sys
import os
from dotenv import load_dotenv
import openpyxl
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



    pkg_no, pkg_name, location, budget, estimated_cost, quantity, unit = str(read_cell_value('G15')), str(read_cell_value('G16')), str(read_cell_value('G17')), str(read_cell_value('G18')), str(read_cell_value('G19')), str(read_cell_value('G21')), str(read_cell_value('G22'))

    financial_year, budget_type, approval_status, app_id, tender_type = str(read_cell_value('G26')), str(read_cell_value('G27')), str(read_cell_value('G28')), str(read_cell_value('G29')), str(read_cell_value('G32'))
    procur_nature, emrgency, app_cost, approv_authority, procure_type = str(read_cell_value('G33')), str(read_cell_value('G34')), str(read_cell_value('G35')), str(read_cell_value('G39')), str(read_cell_value('G40'))
    procure_method, exp_ift_dt, submsn_duration, opening_duration, eval_submn_duration = str(read_cell_value('G41')), str(read_cell_value('G44').strftime("%d/%m/%Y")), str(read_cell_value('G45')), str(read_cell_value('G46')), str(read_cell_value('G47'))
    contract_aproval_duration, noa_duration, contr_sign_durataion, contr_comp_duration = str(read_cell_value('G48')), str(read_cell_value('G49')), str(read_cell_value('G50')), str(read_cell_value('G51'))

    notice_memo_date, publish_datetime, last_sell_datetime, meeting_start_datetime = str(read_cell_value('G58')), str(read_cell_value('G60').strftime("%d/%m/%Y %H:%M")), str(read_cell_value('G61').strftime("%d/%m/%Y %H:%M")), str(read_cell_value('G63').strftime("%d/%m/%Y %H:%M"))
    meeting_end_datetime, closing_datetime, security_subnm_datetime, eligibility, brief_desc, tender_security_bdt = str(read_cell_value('G64').strftime("%d/%m/%Y %H:%M")), str(read_cell_value('G66').strftime("%d/%m/%Y %H:%M")), str(read_cell_value('G69').strftime("%d/%m/%Y %H:%M")), str(read_cell_value('G72')), str(read_cell_value('G74')), str(read_cell_value('G76')) 
    work_start_date, work_end_date, approving_authority, standard_document, tender_validity = str(read_cell_value('G78').strftime("%d/%m/%Y")), str(read_cell_value('G79').strftime("%d/%m/%Y")), str(read_cell_value('G81')), str(read_cell_value('G83')), str(read_cell_value('G84'))

    tender_id  = str(read_cell_value('G57'))
    tender_plotter = EgpTenderPlotter(website_url, email_address, email_password)


    print(f"package information of {pkg_no} loaded.")

    package_info = PackageDetails(pkg_no, pkg_name, location, budget, estimated_cost, quantity, unit)
    package_app = AppPackage(financial_year, budget_type, approval_status, app_id, tender_type, 
                 procur_nature, emrgency, app_cost, approv_authority, procure_type, 
                 procure_method, exp_ift_dt, submsn_duration, opening_duration, eval_submn_duration,
                 contract_aproval_duration, noa_duration, contr_sign_durataion, contr_comp_duration)
    tender_notice = TenderNotice (notice_memo_date, publish_datetime, last_sell_datetime, meeting_start_datetime,
                 meeting_end_datetime, closing_datetime, security_subnm_datetime, eligibility, brief_desc, tender_security_bdt,
                 work_start_date, work_end_date, approving_authority, standard_document, tender_validity)
    
    try:
        if tender_plotter.load_website():
            if tender_plotter.login():
                tender_plotter.close_popup()
                tender_plotter.select_my_tender_submenu(True)
                tender_plotter.select_a_package_from_under_preparation_tab(tender_id)
                
                print(f"Plotting tender for Package No.: {package_info.pkg_no}.")
                tender_plotter.prepare_tender_notice(package_info, tender_notice)
                
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

