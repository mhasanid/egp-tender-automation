import sys
import os
from dotenv import load_dotenv
import openpyxl
from egp_tender_plotter import EgpTenderPlotter, TenderDataSheet, TenderPCC


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

    

    tender_id  = str(read_cell_value('G57'))
    pkg_no = str(read_cell_value('G15'))

    std_document, general_info, fund_source, dev_partner, eligible_country = str(read_cell_value('G83')), str(read_cell_value('G93')), str(read_cell_value('G94')), str(read_cell_value('G95')), str(read_cell_value('G96'))
    eligible_materials, clarify_etd, pretender_meeting, pretender_meeting_time, similar_experience, turnover = str(read_cell_value('G97')), str(read_cell_value('G100')), str(read_cell_value('G101')), str(read_cell_value('G102')), str(read_cell_value('G105')), str(read_cell_value('G106')) 
    liquid_asset, tender_capacity, personnel_capacity, equipment_capacity, jvca, jvca_clause, subcontract_info = str(read_cell_value('G107')), str(read_cell_value('G108')),str(read_cell_value('G110')),str(read_cell_value('G111')), str(read_cell_value('G112')),str(read_cell_value('G113')),str(read_cell_value('G114')),
    additional_docs, price_adjuctment, submission_deadline = str(read_cell_value('G117')), str(read_cell_value('G118')), str(read_cell_value('G121'))

    work_start_date, days_to_complete, site_location, drawings_no, days_to_start_work = str(read_cell_value('G129').strftime("%d/%m/%Y")), str(read_cell_value('G130')), str(read_cell_value('G131')), str(read_cell_value('G132')), str(read_cell_value('G133'))
    site_possession_date, work_summary, other_documents, eligible_country_pcc, eligible_materials_pcc = str(read_cell_value('G134').strftime("%d/%m/%Y")), str(read_cell_value('G135')), str(read_cell_value('G136')), str(read_cell_value('G137')), str(read_cell_value('G138'))
    site_possession, days_to_submit_work_programme, work_prog_update_days, work_prog_late_submn_fee = str(read_cell_value('G139')), str(read_cell_value('G140')), str(read_cell_value('G141')), str(read_cell_value('G142'))
    defect_liability_months, price_adjustment, performance_security, liquid_damage_per_day = str(read_cell_value('G143')), str(read_cell_value('G144')), str(read_cell_value('G145')), str(read_cell_value('G147'))
    liquid_damage_max, advance_amount, as_built_drawing_days, onm_days, as_built_drawing_late_fee = str(read_cell_value('G148')), str(read_cell_value('G149')), str(read_cell_value('G150')), str(read_cell_value('G151')), str(read_cell_value('G152'))
    termination_payment_percent, adjud_name, adjud_address, adjud_phone, adjud_fax, arbitration_place = str(read_cell_value('G153')), str(read_cell_value('G154')), str(read_cell_value('G155')), str(read_cell_value('G156')), str(read_cell_value('G157')), str(read_cell_value('G159'))

    # Create an instance of EgpTenderPlotter
    tender_plotter = EgpTenderPlotter(website_url, email_address, email_password)

    print(f"package information of {pkg_no} loaded.")
       
    tender_datasheet = TenderDataSheet(std_document, general_info, fund_source, dev_partner, eligible_country,
                 eligible_materials, clarify_etd, pretender_meeting, pretender_meeting_time, similar_experience, turnover,
                 liquid_asset, tender_capacity, personnel_capacity, equipment_capacity, jvca, jvca_clause, subcontract_info,
                 additional_docs, price_adjuctment, submission_deadline)
    
    tender_pcc = TenderPCC(work_start_date, days_to_complete, site_location, drawings_no, days_to_start_work,
                 site_possession_date, work_summary, other_documents, eligible_country_pcc, eligible_materials_pcc,
                 site_possession, days_to_submit_work_programme, work_prog_update_days, work_prog_late_submn_fee,
                 defect_liability_months, price_adjustment, performance_security, liquid_damage_per_day,
                 liquid_damage_max, advance_amount, as_built_drawing_days, onm_days, as_built_drawing_late_fee,
                 termination_payment_percent, adjud_name, adjud_address, adjud_phone, adjud_fax, arbitration_place)

    try:
        if tender_plotter.load_website():
            if tender_plotter.login():
                tender_plotter.close_popup()
                tender_plotter.select_my_tender_submenu(True)
                tender_plotter.select_a_package_from_under_preparation_tab(tender_id)
                
                print(f"Tender Documents for Pkg No. {pkg_no} will be prepared.")
                tender_plotter.prepare_tender_document_tds(tender_datasheet)
                tender_plotter.prepare_tender_document_pcc(tender_pcc)
                
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

