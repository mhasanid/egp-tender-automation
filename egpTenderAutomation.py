import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from egpXpathConstants import EgpXpaths
from inputOptions import BudgetType
from datetime import date

class EgpTenderPlotter:

    def __init__(self, url, email, password):
        self.url = url
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 10)  # Set the maximum wait time
        
    def load_website(self):
        try:
            self.driver.get(self.url)
            # Waiting for an element of the website (here login button) to load.
            self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.LOGIN_BTN_XPATH)))
            print(f"\nThe website: {self.url} is loaded successfully.")
            return True
            
        except TimeoutException:
            print(f"\nTimeout while loading the website: {self.url}")
            return False

    # login() returns boolean
    def login(self):
        try:
            # Wait until the email input field is present and then populate
            email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.EMAIL_INPUT_XPATH)))
            email_input.send_keys(self.email)
            
            # Wait until the password input field is present and then populate
            password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PASSWORD_INPUT_XPATH)))
            password_input.send_keys(self.password)
            
            # Submit the login form if the login button is loaded.
            login_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.LOGIN_BTN_XPATH)))
            login_btn.click()

            print("User successfully Logged in.")
            return True
            
        except TimeoutException:
            print("\nTimeout while waiting for login elements.")
            return False
    
    def close_popup(self):
        try:
            # Wait until the Popup box appear 
            popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH))) 
            popup_ok_btn.click()
            print("Closing Popup: done.")
            
        except TimeoutException:
            print("Closing Popup: No Popup found.")

    def select_create_app_submenu(self):
        try:
            # Wait until the main menu is present and then hover over it
            main_menu_app = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_MENU_XPATH)))
            ActionChains(self.driver).move_to_element(main_menu_app).perform()

            # Wait until the submenu is present and then click it
            submenu_create_app = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CREATE_APP_SUBMENU_XPATH)))
            submenu_create_app.click()

            print("Navigated to: Create APP Page")

        except TimeoutException:
            print("Navigating Error: Create APP Page")

    def select_my_app_submenu(self):
        try:
            self.wait.until(
                lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)")
            )

            # Wait until the main menu is present and then hover over it
            main_menu_app = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_MENU_XPATH)))
            ActionChains(self.driver).move_to_element(main_menu_app).perform()

            # Wait until the submenu is present and then click it
            submenu_my_app = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MYAPP_SUBMENU_XPATH)))
            submenu_my_app.click()

            print("Navigated to: My APP Page")

        except TimeoutException:
            print("Navigating Error: My APP Page")

    def create_app(self, financial_year, budget_type, app_code):
        try:
            # Wait until the Budget Type dropdown appear 
            budget_type_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CREATE_APP_BUDGET_TYPE_XPATH))) 
            select_budget_type = Select(budget_type_dropdown)
            select_budget_type.select_by_visible_text(budget_type)

            # Wait until the FY dropdown appear 
            financial_year_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CREATE_APP_FY_XPATH))) 
            select_fy = Select(financial_year_dropdown)
            select_fy.select_by_visible_text(financial_year)

            # Wait until the APP id textbox appear 
            app_code_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CREATE_APP_CODE_XPATH)))
            app_code_input.send_keys(app_code)

            # Creating APP by clicking the Next button after the Next button is loaded.
            create_app_next_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CREATE_APP_NEXT_BTN_XPATH)))
            create_app_next_btn.click()

            self.wait.until(
                lambda x: x.execute_script("return document.readyState === 'complete'")
            )

            if "App is already exist" in self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CREATE_APP_ERROR_PLACEHOLDER_XPATH))).text:
                return False
            else:
                print ("Create APP: Successful")
                
        except TimeoutException:
            print ("Create APP: Problem creating APP.")
            return False

    def select_app(self, financial_year, budget_type, status, app_id):
        # This function assume that the User currently is in the My APP Page.
        try:
            # Wait until the FY dropdown appear 
            financial_year_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MYAPP_FY_XPATH))) 
            select_fy = Select(financial_year_dropdown)
            select_fy.select_by_visible_text(financial_year)

            # Wait until the Budget Type dropdown appear 
            budget_type_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MYAPP_BUDGET_TYPE_XPATH))) 
            select_budget_type = Select(budget_type_dropdown)
            select_budget_type.select_by_visible_text(budget_type)
            
            # Wait until the Status dropdown appear 
            status_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MYAPP_STATUS_XPATH))) 
            select_status = Select(status_dropdown)
            select_status.select_by_visible_text(status)

            # Wait until the APP id textbox appear 
            app_id_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MYAPP_APP_ID_XPATH)))
            app_id_input.send_keys(app_id)

            # Click the Search button after the Search button is loaded.
            search_app_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_SEARCH_BTN_XPATH)))
            search_app_btn.click()

            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            # Find all rows in the APP search result table
            app_table = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_SEARCH_RESULT_TABLE_XPATH)))
            rows = app_table.find_elements(By.TAG_NAME, "tr")
            # Debugging
            # print(f"{app_table.get_attribute("innerHTML")}")    
                
            
            desired_app = None
            for row in rows:
                # Debugging
                # print(f"APP found at row :{row.get_attribute("innerHTML")}")    
                cell_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                
                if app_id in cell_text:
                    desired_app = row
                    break

            # Perform actions on the desired row, for example, click a button within the row
            if desired_app:
                button_within_row = desired_app.find_element(By.CSS_SELECTOR, "td:nth-child(6) > a")
                button_within_row.click()



        except TimeoutException:
            print("My APP: Problem Setting Searching Criteria.")

    # add_project_to_app() returns boolean
    def add_project_to_app(self):
            # This function assume that the User currently is in the desired APP.
            try:
                # Wait until the FY dropdown appear 
                add_new_pkg_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.ADD_NEW_PKG_BTN_XPATH))) 
                add_new_pkg_btn.click()
                
                # Wait until the page loading complete.
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Selecting tender type.
                tender_type = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_TYPE))) 
                select_tender_type = Select(tender_type)
                select_tender_type.select_by_visible_text("Manual")

                # Selecting procurement nature.
                procurement_nature = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PROCUR_NATURE))) 
                select_procurement_nature = Select(procurement_nature)
                select_procurement_nature.select_by_visible_text("Works")

                # Selecting Emergency Type.
                emergency_type = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EMERGENCY_TYPE))) 
                select_emergency_type = Select(emergency_type)
                select_emergency_type.select_by_visible_text("Normal")

                # Inserting Package No.
                package_no_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_NO)))
                package_no_input.send_keys("NDR/DPM/23-24/W-40")

                # Package No Uniqueness check.
                package_no_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_NO_MSG)))
                package_no_msg.click()

                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                if "OK" in package_no_msg.text:
                    # Inserting Package Description.
                    package_description = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_DESCRIPTION)))
                    package_description.send_keys("Re-construction & Repair of irrigation dyke respectively from km. 2.200 to km. 3.200 = 1000 m. at R/B of Main Khal (Saitpakiya Khal) of NP-1 Pump House at Nalcity upazilla of Jhalakathi District under Jhalakathi WD Division, BWDB, Jhalakathi from NDR budget during The FY 2023-2024")

                    # Inserting Lot No.
                    lot_no_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_LOT_NO)))
                    lot_no_input.send_keys("NDR/DPM/23-24/W-40")

                    # Inserting Lot Description.
                    lot_description = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_LOT_DESCRIPTION)))
                    lot_description.send_keys("Re-construction & Repair of irrigation dyke respectively from km. 2.200 to km. 3.200 = 1000 m. at R/B of Main Khal (Saitpakiya Khal) of NP-1 Pump House at Nalcity upazilla of Jhalakathi District under Jhalakathi WD Division, BWDB, Jhalakathi from NDR budget during The FY 2023-2024")

                    # Inserting Lot No.
                    quantity_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_QUANTITY)))
                    quantity_input.send_keys("40")

                    # Inserting Lot No.
                    unit_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_UNIT)))
                    unit_input.send_keys("meter")

                    # Inserting Lot No.
                    app_est_cost_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EST_COST)))
                    app_est_cost_input.send_keys("405000")


                    # Selecting approving authority.
                    approving_authority = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_APPROVING_AUTHORITY))) 
                    select_approving_authority = Select(approving_authority)
                    select_approving_authority.select_by_visible_text("PE")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Selecting PQ Requires.
                    pq_req = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PQ_REQUIRES))) 
                    select_pq_req = Select(pq_req)
                    select_pq_req.select_by_visible_text("No")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Selecting Procurement Type.
                    procurement_type = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PROCUR_TYPE))) 
                    select_procurement_type = Select(procurement_type)
                    select_procurement_type.select_by_visible_text("NCT")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Selecting Procurement Method.
                    procurement_method = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PROCURE_METHOD))) 
                    select_procurement_method = Select(procurement_method)
                    select_procurement_method.select_by_visible_text("Open Tendering Method")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Select Category.
                    category = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_SELECT_CATEGORIES)))
                    category.click()
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Switching to Category Window.
                    main_window_handle = self.driver.window_handles[0]
                    category_window_handle = self.driver.window_handles[1]
                    self.driver.switch_to.window(category_window_handle)


                    # Select construction work.
                    category_construction_work = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_CATEGORY_CONSTR_WORK_TREE)))
                    category_construction_work.click()

                    # Select civil work.
                    category_civil_work = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_CATEGORY_CIVIL_WORK_TREE)))
                    category_civil_work.click()

                    # Select water project.
                    category_water_project = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_CATEGORY_WATER_PROJECT_TREE)))
                    category_water_project.click()

                    # Submit category.
                    category_water_project = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_CATEGORY_SUBMIT_BTN)))
                    category_water_project.click()

                    # Switching bank to Main Window.
                    self.driver.switch_to.window(main_window_handle)
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Creatng APP and Go to Next.
                    add_package_btn  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_NEXT_BTN)))
                    add_package_btn.click()
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Select Expected e-GP IFT.
                    expected_ift_datepicker_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_EGP_IFT_DATEPICKER)))
                    # expected_ift_datepicker.click()
                    self.driver.execute_script("arguments[0].removeAttribute('readonly')", expected_ift_datepicker_input)
                    expected_ift_datepicker_input.send_keys("07/03/2024")
                    self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", expected_ift_datepicker_input)
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------
                    
                    
                    # Insert Last Tender Submission Duration.
                    expected_tender_sub_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_LAST_SUBMISSION_INPUT)))
                    expected_tender_sub_duration_input.send_keys("14")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Insert Last Tender Opening Duration.
                    expected_opening_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_OPENING_INPUT)))
                    expected_opening_duration_input.send_keys("7")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Last Tender Evaluation Duration.
                    expected_evaluation_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_EVALUATION_SUB_INPUT)))
                    expected_evaluation_duration_input.clear()
                    expected_evaluation_duration_input.send_keys("14")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Approval for Award of Contract Duration.
                    expected_approval_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_APPROVAL_INPUT)))
                    expected_approval_duration_input.clear()
                    expected_approval_duration_input.send_keys("7")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Issuance of the NOA Duration.
                    expected_noa_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_NOA_ISSUE_INPUT)))
                    expected_noa_duration_input.clear()
                    expected_noa_duration_input.send_keys("7")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Signing of Contract Duration.
                    expected_contract_signing_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_CONTRACT_SIGNING_INPUT)))
                    expected_contract_signing_input.send_keys("7")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Completion of Contract Duration.
                    expected_contract_completion_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_WORK_COMPLETION_DURATION_INPUT)))
                    expected_contract_completion_input.send_keys("30")
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Saving the Package in APP.
                    save_package_btn  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_SAVE)))
                    save_package_btn.click()
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    return True
                else:
                    print(package_no_msg.text)
                    return False


            except TimeoutException:
                print("My APP: Problem Setting Searching Criteria.")
                return False


    # def prepare_tender_from_under_prep(self, financial_year, budget_type, status, app_id, tender_id):
    def prepare_tender_from_under_prep(self):
        try:
            self.wait.until(
                lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)")
            )
            # Wait until the main menu is present and then hover over it
            main_menu_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_MENU_XPATH)))
            ActionChains(self.driver).move_to_element(main_menu_tender).perform()

            # Wait until the submenu is present and then click it
            submenu_my_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MY_TENDER_SUBMENU_XPATH)))
            submenu_my_tender.click()

            print("Navigated to: My Tender Page")

            # Navigating to Under Preparation Tab:
            self.wait.until(
                lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)")
            )
            processing_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UNDER_PREPARATION_TAB)))
            processing_tender.click()
            
            self.wait.until(
                lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)")
            )


        except TimeoutException:
            print("My Tender: Problem.")

    
    def quit(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    
    # EGP Credentials
    website_url = "https://www.eprocure.gov.bd/"
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("PASSWORD")
    
    # Create an instance of EgpTenderPlotter
    tender_plotter = EgpTenderPlotter(website_url, email_address, email_password)
    
    try:
        # If the website loaded then do other things.
        if tender_plotter.load_website():

            # Log in to e-GP Portal
            if tender_plotter.login():
                tender_plotter.close_popup()
                tender_plotter.select_my_app_submenu()
                tender_plotter.select_app("2023-2024", "Revenue", "- Approved -", "199797")
                tender_plotter.add_project_to_app()
                # tender_plotter.prepare_tender_from_under_prep()

                # tender_plotter.select_create_app_submenu()
                
                # new_appid = tender_plotter.create_app("2012-2013", BudgetType.REVENUE.value, "NDR/2010-2011")
                # if new_appid:
                #     print(f"New APP is created.")
                # else:
                #     print("APP is not created.")

                # tender_plotter.select_app("92473")

                print("Do other things.")
            else:
                print("Unable to login to the EGP System.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        input("\nPress Enter to close the browser...")
        tender_plotter.quit()
