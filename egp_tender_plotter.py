import os
import time
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
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException, StaleElementReferenceException, NoSuchElementException
from utility import Utility

class EgpTenderPlotter:

    def __init__(self, url, email, password, headless=None):

        # Set Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.url = url
        self.email = email
        self.password = password
        
        if(headless == "headless"):
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 60)  # Set the maximum wait time
        
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
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH))) 
            popup_ok_btn.click()
            print("Closing Popup: done.")
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

        except TimeoutException:
            print("Closing Popup: No Popup found.")

    def update_info_later(self):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UPDATE_LATER_BTN_XPATH))) 
            popup_ok_btn.click()
            print("Update Info Later selected.")
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

        except TimeoutException:
            print("Update Later: No Button found.")

    def select_create_app_submenu(self):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
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
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            # Wait until the main menu is present and then hover over it
            main_menu_app = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_MENU_XPATH)))
            ActionChains(self.driver).move_to_element(main_menu_app).perform()

            # Wait until the submenu is present and then click it
            submenu_my_app = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MYAPP_SUBMENU_XPATH)))
            submenu_my_app.click()

            print("Navigated to: My APP Page")

        except TimeoutException:
            print("Navigating Error: My APP Page")

    def select_my_tender_submenu(self, pe_user):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            # Wait until the main menu is present and then hover over it
            main_menu_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_MENU_XPATH)))
            ActionChains(self.driver).move_to_element(main_menu_tender).perform()

            # Wait until the submenu is present and then click it
            if pe_user:
                submenu_my_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MY_TENDER_SUBMENU_PE_XPATH)))
            else:
                submenu_my_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.MY_TENDER_SUBMENU_OTHER_XPATH)))
            
            submenu_my_tender.click()

            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            print("Navigated to: My Tender Page")
          
        except TimeoutException:
            print("Navigating Error:My Tender Page")

    def select_a_package_from_under_preparation_tab(self, tender_id):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            tender_id_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_ID_INPUT)))
            tender_id_input.clear()
            tender_id_input.send_keys(tender_id) # duration for Approval for Award of Contract
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------


            processing_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UNDER_PREPARATION_TAB)))
            processing_tender.click()
            
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # Find all rows in the APP search result table
            tender_search_rslt_table = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_SEARCH_RESULT_TABLE))) #//*[@id='resultTable']/tbody
            rows = tender_search_rslt_table.find_elements(By.TAG_NAME, "tr")

            desired_package = None
            for row in rows:
                # Debugging
                # print(f"APP found at row :{row.get_attribute("innerHTML")}")    
                cell_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                
                if tender_id in cell_text:
                    desired_package = row
                    break

            # Perform actions on the desired row, for example, click a button within the row
            if desired_package:
                button_within_row = desired_package.find_element(By.CSS_SELECTOR, "td:nth-child(7) > a") 
                button_within_row.click()
                return True
            else:
                return False
          
        except TimeoutException:
            print("Navigating Error: Tender Under Preparation Page")
            return False


    def select_a_package_from_processing_tab(self, tender_id):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            tender_id_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_ID_INPUT)))
            tender_id_input.clear()
            tender_id_input.send_keys(tender_id) # duration for Approval for Award of Contract
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------


            processing_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PROCESSING_TAB)))
            processing_tender.click()
            
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # Find all rows in the APP search result table
            tender_search_rslt_table = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_SEARCH_RESULT_TABLE))) #//*[@id='resultTable']/tbody
            rows = tender_search_rslt_table.find_elements(By.TAG_NAME, "tr")

            desired_package = None
            for row in rows:
                # Debugging
                # print(f"APP found at row :{row.get_attribute("innerHTML")}")    
                cell_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                
                if tender_id in cell_text:
                    desired_package = row
                    break

            # Perform actions on the desired row, for example, click a button within the row
            if desired_package:
                button_within_row = desired_package.find_element(By.CSS_SELECTOR, "td:nth-child(7) > a") 
                button_within_row.click()
                return True
            else:
                return False
          
        except TimeoutException:
            print("Navigating Error: Tender Processing Page")
            return False



    def select_a_package_from_archived_tab(self, tender_id):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            tender_id_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_ID_INPUT)))
            tender_id_input.clear()
            tender_id_input.send_keys(tender_id) # duration for Approval for Award of Contract
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------


            processing_tender = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.ARCHIVED_TAB)))
            processing_tender.click()
            
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # Find all rows in the APP search result table
            tender_search_rslt_table = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_SEARCH_RESULT_TABLE))) #//*[@id='resultTable']/tbody
            rows = tender_search_rslt_table.find_elements(By.TAG_NAME, "tr")

            desired_package = None
            for row in rows:
                # Debugging
                # print(f"APP found at row :{row.get_attribute("innerHTML")}")    
                cell_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                
                if tender_id in cell_text:
                    desired_package = row
                    break

            # Perform actions on the desired row, for example, click a button within the row
            if desired_package:
                button_within_row = desired_package.find_element(By.CSS_SELECTOR, "td:nth-child(7) > a") 
                button_within_row.click()
                return True
            else:
                return False
          
        except TimeoutException:
            print("Navigating Error: Tender Archived Page")
            return False


    def get_performance_secrity_payment_details(self, tender_id):
        try:
            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            select_payment_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PAYMENT_BTN)))
            select_payment_btn.click()

            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            select_performanc_security_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PERFORMANCE_SECURITY_BTN)))
            select_performanc_security_btn.click()

            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            view_performance_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.VIEW_PERFORMANCE_BTN)))
            view_performance_btn.click()

            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            performance_payment_details = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PERFORMANCE_PAYMENT_DETAILS_BY_CONTRACTOR_BTN)))
            performance_payment_details.click()

            # ---------------------------------------------------------------------------------------------------------------
            # Waiting for loading to be completed. 
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            payment_details_dict = {}
            tender_id_label = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_ID_LABEL))).text

            
            if tender_id_label in tender_id:
                 # Find all rows in the APP search result table
                payment_details_table = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PERFORMANCE_PAYMENT_DETAILS_TABLE))) 
                rows = payment_details_table.find_elements(By.TAG_NAME, "tr")

                for index, row in enumerate(rows):
                    payment_details_dict [row.find_element(By.XPATH, "//*[@id='print_area']/div[2]/table/tbody/tr["+str(index+1)+"]/td[1]").text] = row.find_element(By.XPATH, "//*[@id='print_area']/div[2]/table/tbody/tr["+str(index+1)+"]/td[2]").text
                
                return payment_details_dict
            else:
                return False
            

          
        except TimeoutException:
            print("Navigating Error: Time out Loading- Tender Archived Page")
            return False


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

            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------



        except TimeoutException:
            print("My APP: Problem Setting Searching Criteria.")

    # add_project_to_app() returns boolean
    def add_project_to_app(self, package_detail, package_app):
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
                select_tender_type.select_by_visible_text(package_app.tender_type)  # e-GP/Mannual 

                # Selecting procurement nature.
                procurement_nature = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PROCUR_NATURE))) 
                select_procurement_nature = Select(procurement_nature)
                select_procurement_nature.select_by_visible_text(package_app.procur_nature) # Goods/Works

                # Selecting Emergency Type.
                emergency_type = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EMERGENCY_TYPE))) 
                select_emergency_type = Select(emergency_type)
                select_emergency_type.select_by_visible_text(package_app.emrgency) # Normal/Urgent(Catastrophe)/National disaster

                # Inserting Package No.
                package_no_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_NO)))
                package_no_input.send_keys(package_detail.pkg_no)

                # Package No Uniqueness check.
                package_no_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_NO_MSG)))
                package_no_msg.click()

                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                if "OK" in package_no_msg.text:

                    print(f"Adding Package No. {package_detail.pkg_no} to APP.")

                    # Inserting Package Description.
                    package_description = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PKG_DESCRIPTION)))
                    package_description.send_keys(package_detail.pkg_name)

                    # Inserting Lot No.
                    lot_no_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_LOT_NO)))
                    lot_no_input.send_keys(package_detail.pkg_no)

                    # Inserting Lot Description.
                    lot_description = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_LOT_DESCRIPTION)))
                    lot_description.send_keys(package_detail.pkg_name)

                    # Inserting Quantity of Works/Goods.
                    quantity_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_QUANTITY)))
                    quantity_input.send_keys(package_detail.quantity)

                    # Inserting unit of Quantity.
                    unit_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_UNIT)))
                    unit_input.send_keys(package_detail.unit)

                    # Inserting APP Cost.
                    app_est_cost_input = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EST_COST)))
                    app_est_cost_input.send_keys(package_app.app_cost)  # APP Cost


                    # Selecting approving authority.
                    approving_authority = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_APPROVING_AUTHORITY))) 
                    select_approving_authority = Select(approving_authority)
                    select_approving_authority.select_by_visible_text(package_app.approv_authority) # Approving Authority = PE/AO/HOPE
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
                    select_procurement_type.select_by_visible_text(package_app.procure_type) # Procurement Type = NCT/ICT
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Selecting Procurement Method.
                    procurement_method = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_PROCURE_METHOD))) 
                    select_procurement_method = Select(procurement_method)
                    select_procurement_method.select_by_visible_text(package_app.procure_method) # Procurement Method = OTM/DPM/RFQ etc.
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
                    expected_ift_datepicker_input.send_keys(package_app.exp_ift_dt) # Date of IFT
                    self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", expected_ift_datepicker_input)
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------
                    
                    
                    # Insert Last Tender Submission Duration.
                    expected_tender_sub_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_LAST_SUBMISSION_INPUT)))
                    expected_tender_sub_duration_input.clear()
                    expected_tender_sub_duration_input.send_keys(package_app.submsn_duration) # duration for tender submission
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    # Insert Last Tender Opening Duration.
                    expected_opening_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_OPENING_INPUT)))
                    expected_opening_duration_input.clear()
                    expected_opening_duration_input.send_keys(package_app.opening_duration) # duration for tender opening
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    '''
                    # Insert Last Tender Evaluation Duration.
                    expected_evaluation_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_EVALUATION_SUB_INPUT)))
                    expected_evaluation_duration_input.clear()
                    expected_evaluation_duration_input.send_keys(package_app.eval_submn_duration) # duration for tender evaluation
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Approval for Award of Contract Duration.
                    expected_approval_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_APPROVAL_INPUT)))
                    expected_approval_duration_input.clear()
                    expected_approval_duration_input.send_keys(package_app.contract_aproval_duration) # duration for Approval for Award of Contract
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Issuance of the NOA Duration.
                    expected_noa_duration_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_NOA_ISSUE_INPUT)))
                    expected_noa_duration_input.clear()
                    expected_noa_duration_input.send_keys(package_app.noa_duration) # duration for NOA
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------
                    '''

                    # Insert Signing of Contract Duration.
                    expected_contract_signing_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_CONTRACT_SIGNING_INPUT)))
                    expected_contract_signing_input.clear()
                    expected_contract_signing_input.send_keys(package_app.contr_sign_durataion) # duration for Signing of Contract
                    # Wait until the page loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------


                    # Insert Completion of Contract Duration.
                    expected_contract_completion_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_ADD_PKG_EXPECTED_WORK_COMPLETION_DURATION_INPUT)))
                    expected_contract_completion_input.clear()
                    expected_contract_completion_input.send_keys(package_app.contr_comp_duration ) # duration for Completion of Contract
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

                    # Find all rows in the APP search result table
                    app_pkgs_table = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APP_PKGS_LIST_TABLE)))
                    rows = app_pkgs_table.find_elements(By.TAG_NAME, "tr")

                    inserted_pkg = None
                    for row in rows:
                        # Debugging
                        # print(f"APP found at row :{row.get_attribute("innerHTML")}")
                        # Skipped first Two Rows of the Package List Table for headers with the following condition. 
                        if rows.index(row)>=1 and rows.index(row)< len(rows):    
                            cell_text = row.find_element(By.XPATH, "//*[@id='resultTable']/tbody/tr["+str(rows.index(row)+1)+"]/td[2]").text
                            if package_detail.pkg_no in cell_text:
                                inserted_pkg = row.find_element(By.XPATH, "//*[@id='resultTable']/tbody/tr["+str(rows.index(row)+1)+"]/td[1]").text
                                break

                    if inserted_pkg:
                        print(f"Pkg No. {package_detail.pkg_no} added successfully to the APP at SL No. {inserted_pkg}")
                        return True
                    else:
                        print(f"Pkg No. {package_detail.pkg_no} could not be inserted into the APP")
                        return False

                else:
                    print(package_no_msg.text)
                    return False


            except TimeoutException:
                print("My APP: Problem Setting Searching Criteria.")
                return False


    # def prepare_tender_from_under_prep(self, financial_year, budget_type, status, app_id, tender_id):
    def prepare_tender_notice(self, package_info, tender_notice):
        try:
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            # Navigating to Notice Tab:
            tender_notice_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_NOTICE_TAB)))
            tender_notice_tab.click()
            
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            
            # Clicking on Edit Button (notice):
            edit_tender_notice_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_NOTICE_EDIT_BTN)))
            edit_tender_notice_btn.click()
            
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # Insert invitation ref memo and date.
            invitation_ref_memo_date  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.INVITATION_REFERENCE_NO_INPUT)))
            invitation_ref_memo_date.clear()
            invitation_ref_memo_date.send_keys(tender_notice.notice_memo_date) 
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # time.sleep(3)
            # Insert Tender/Proposal Publication Date and Time.
            tender_publish_datetime_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_PUBLICATION_DATE_TIME_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", tender_publish_datetime_input)
            tender_publish_datetime_input.clear()
            # tender_publish_datetime_input.click()
            tender_publish_datetime_input.send_keys(tender_notice.publish_datetime)
            # tender_publish_datetime_input.send_keys(Keys.ENTER)
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", tender_publish_datetime_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # time.sleep(3)
            # Insert Last Selling Date and Time.
            last_selling_datetime_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_LAST_SELLING_DATE_TIME_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", last_selling_datetime_input)
            last_selling_datetime_input.clear()
            # last_selling_datetime_input.click()
            last_selling_datetime_input.send_keys(tender_notice.last_sell_datetime)
            # last_selling_datetime_input.send_keys(Keys.ENTER)
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", last_selling_datetime_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # time.sleep(3)
            # Insert Pre-Tender Meeting Start Date and Time.
            meeting_start_datetime_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PRE_TENDER_MEETING_START_DATE_TIME_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", meeting_start_datetime_input)
            meeting_start_datetime_input.clear()
            # meeting_start_datetime_input.click()
            meeting_start_datetime_input.send_keys(tender_notice.meeting_start_datetime) 
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", meeting_start_datetime_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # time.sleep(3)
            # Insert Pre-Tender Meeting End Date and Time.
            meeting_end_datetime_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PRE_TENDER_MEETING_END_DATE_TIME_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", meeting_end_datetime_input)
            meeting_end_datetime_input.clear()
            # meeting_end_datetime_input.click()
            meeting_end_datetime_input.send_keys(tender_notice.meeting_end_datetime) 
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", meeting_end_datetime_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------


            # time.sleep(3)
            # Insert Tender Closing Date and Time.
            tender_closing_datetime_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_CLOSING_DATE_TIME_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", tender_closing_datetime_input)
            tender_closing_datetime_input.clear()
            # tender_closing_datetime_input.click()
            tender_closing_datetime_input.send_keys(tender_notice.closing_datetime)
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", tender_closing_datetime_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            # time.sleep(3)
            # Insert Tender Security Submission Last Date and Time.
            security_submn_datetime_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_SECURITY_SUBMN_DATE_TIME_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", security_submn_datetime_input)
            security_submn_datetime_input.clear()
            # security_submn_datetime_input.click()
            security_submn_datetime_input.send_keys(tender_notice.security_subnm_datetime)
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", security_submn_datetime_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
        
            
            # time.sleep(3)
            # Insert Location of the project.
            location_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.LOCATION_OF_WORK_INPUT)))
            location_input.clear()
            # location_input.click()
            location_input.send_keys(package_info.location)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            #===================       

            # time.sleep(3)
            # Insert Tentative Work Start Date.
            tentative_work_start_date_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENTATIVE_WORK_START_DATE_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", tentative_work_start_date_input)
            tentative_work_start_date_input.clear()
            # tentative_work_start_date_input.click()
            tentative_work_start_date_input.send_keys(tender_notice.work_start_date) 
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", tentative_work_start_date_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            # time.sleep(3)
            # Insert Tentative Work End Date.
            tentative_work_end_date_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENTATIVE_WORK_END_DATE_INPUT)))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", tentative_work_end_date_input)
            tentative_work_end_date_input.clear()
            # tentative_work_end_date_input.click()
            tentative_work_end_date_input.send_keys(tender_notice.work_end_date) 
            self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", tentative_work_end_date_input)
            
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------


            # Unfocus
            click_for_unfocus = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmCreateTender']/table[6]/tbody/tr[3]/td")))
            click_for_unfocus.click()
            
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------   
            

            
            # time.sleep(3)
            # Insert Tenderer Eligibility.
            # tenderer_eligibility_iframe  = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")))
            tenderer_eligibility  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.ELIGIBILITY_OF_TENDERER_TXTBOX)))
            # tenderer_eligibility_iframe  = self.wait.until(tenderer_eligibility.find_element((By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")))

            # tenderer_eligibility_iframe = tenderer_eligibility.find_element(By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")
            tenderer_eligibility_iframe = tenderer_eligibility.find_element(By.CSS_SELECTOR, "iframe")

            # Switch to the iframe containing the CKEditor
            self.driver.switch_to.frame(tenderer_eligibility_iframe)

            # tenderer_eligibility_body  = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable")))
            tenderer_eligibility_body  = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
            tenderer_eligibility_body.clear()
            # tenderer_eligibility_body.click()
            # tenderer_eligibility_body.send_keys(tender_notice.eligibility)
            self.driver.execute_script("arguments[0].innerHTML = '"+tender_notice.eligibility+"';", tenderer_eligibility_body)
            self.driver.switch_to.default_content()


            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
                        
            # time.sleep(3)
            # Insert Brief Description.
            # brief_description_iframe  = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")))
            brief_description  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.BRIEF_DESCRIP_OF_WORKS_TXTBOX)))
            brief_description_iframe  = brief_description.find_element(By.CSS_SELECTOR, "iframe")
            
            # Switch to the iframe containing the CKEditor
            self.driver.switch_to.frame(brief_description_iframe)

            # brief_description_body  = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable")))
            brief_description_body  = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
            brief_description_body.clear()
            # brief_description_body.click()
            self.driver.execute_script("arguments[0].innerHTML = '"+tender_notice.brief_desc+"';", brief_description_body)
            # brief_description_body.send_keys(tender_notice.brief_desc)
            
            self.driver.switch_to.default_content()

            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            '''
            # time.sleep(3)
            # Insert Tender Security Amount (in BDT).
            tender_security_bdt_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_SECURITY_INPUT)))
            tender_security_bdt_input.clear()
            # tender_security_bdt_input.click()

            if int(tender_notice.tender_security_bdt)>0:
                for number in tender_notice.tender_security_bdt:
                    time.sleep(0.5)
                    if int(number) == 0: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD0)
                    elif int(number) == 1: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD1)
                    elif int(number) == 2: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD2)
                    elif int(number) == 3: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD3)
                    elif int(number) == 4: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD4)
                    elif int(number) == 5: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD5)
                    elif int(number) == 6: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD6)
                    elif int(number) == 7: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD7)
                    elif int(number) == 8: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD8)
                    elif int(number) == 9: 
                        tender_security_bdt_input.send_keys(Keys.NUMPAD9)
                    
            # tender_security_bdt_input.send_keys(int(tender_notice.tender_security_bdt))
            self.driver.execute_script("arguments[0].blur();", tender_security_bdt_input)
            
            # self.driver.execute_script("arguments[0].value = arguments[1];", tender_security_bdt_input, tender_notice.tender_security_bdt)
            
            time.sleep(2)
            # Wait until the page loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            # ''' 


            user_input = input("Please insert Tender Security manualy and press 'y': ")

            if user_input.lower() == "y":
                
                # Submit Tender Notice
                submit_tender_notice_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, EgpXpaths.NOTICE_SUBMIT_BTN)))
                submit_tender_notice_btn.click()
                
                # Wait until the loading complete.
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------


                # Configure Key Information:
                key_info_create_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.CONFIG_KEY_INFO_CREATE_BTN)))
                key_info_create_btn.click()
                
                # Wait until the loading complete.
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Selecting Approving Authority.
                approving_authority = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.APPROVING_AUTHORITY_INPUT))) 
                select_approving_authority = Select(approving_authority)
                select_approving_authority.select_by_visible_text(tender_notice.approving_authority)
                # Wait until the page loading complete.
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                
                # Selecting Standard Tender Documents.
                standard_document = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.STANDARD_TENDER_DOCUMENT_INPUT))) 
                select_standard_document = Select(standard_document)
                select_standard_document.select_by_visible_text(tender_notice.standard_document) 
                # Wait until the page loading complete.
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------


                # Insert Tender Validity (days).
                tender_validity_input  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_VALIDITY_DAYS_INPUT)))
                tender_validity_input.clear()
                tender_validity_input.send_keys(int(tender_notice.tender_validity))
                # Wait until the page loading complete.
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                user_input = input("Please check if everything is okey. If okey, press 'y': ")
                if user_input.lower() == "y":
                    print("Tender Notice created.")
                    '''
                    # Submit STD
                    submit_std_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, EgpXpaths.SUBMIT_STD_BTN)))
                    submit_std_btn.click()
                    
                    # Wait until the loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------

                    self.wait.until(EC.alert_is_present())
                    try:
                        while True:
                            alert = self.driver.switch_to.alert
                            alert.accept()
                            self.driver.switch_to.default_content()
                    except NoAlertPresentException:
                        print("No alert present.")

                    
                    # Save Section,
                    save_section_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, EgpXpaths.SAVE_FIRST_SECTION_BTN)))
                    save_section_btn.click()
                    
                    # Wait until the loading complete.
                    # ---------------------------------------------------------------------------------------------------------------
                    self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                    # ---------------------------------------------------------------------------------------------------------------
                    #'''


        except Exception:
            print("There is a problem.")

    
    def prepare_tender_document_tds(self, tender_datasheet):
        try:
            # Wait until the loading complete.
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            # Navigating to Document Tab:
            tender_document_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_DOCUMENT_TAB)))
            tender_document_tab.click()
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            

            std_document = tender_datasheet.std_document.find("e-PW3")
            if std_document != -1:
                
                # Tender Data Sheet
                # Clicking on Edit Button (TDS):
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                edit_tender_datasheet_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_DATA_SHEET_EDIT_BTN)))
                edit_tender_datasheet_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                # '''
                # Sub Section A. General
                # =======================================
                # Clicking on Edit Button:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                edit_section_one_general_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_ONE_GENERAL_EDIT_BTN)))
                edit_section_one_general_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Insert General Info.
                general_info_table  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_ONE_GENERAL_TDS_TABLE)))
                rows = general_info_table.find_elements(By.TAG_NAME, "tr")

                for index, row in enumerate(rows):

                    if(row.text.find("1.1 The Procuring Entity named in the Tender Data Sheet (TDS)"))>-1:
                        # Wait until the loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                        general_info_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(general_info_iframe)

                        general_info_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        general_info_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.general_info+"';", general_info_body)

                        self.driver.switch_to.default_content()

                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------


                    if(row.text.find("3.1 PE has been allocated public funds"))>-1:
                        # Wait until the loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                        source_of_fund_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(source_of_fund_iframe)

                        source_of_fund_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        source_of_fund_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.fund_source+"';", source_of_fund_body)

                        self.driver.switch_to.default_content()

                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------


                    if(row.text.find("3.3 Payments by the Development Partner"))>-1:
                        # Wait until the loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                        development_partner_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(development_partner_iframe)

                        development_partner_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        development_partner_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.dev_partner+"';", development_partner_body)

                        self.driver.switch_to.default_content()

                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------


                    if(row.text.find("5.1 This Invitation for Tenders is open"))>-1:
                        # Wait until the loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                        eligibility_country_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(eligibility_country_iframe)

                        eligibility_country_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        eligibility_country_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.eligible_country+"';", eligibility_country_body)

                        self.driver.switch_to.default_content()

                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------


                    if(row.text.find("6.1 All materials, equipment and associated services"))>-1:
                        # Wait until the loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                        eligible_materials_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(eligible_materials_iframe)

                        eligible_materials_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        eligible_materials_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.eligible_materials+"';", eligible_materials_body)

                        self.driver.switch_to.default_content()

                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                # Clicking on Update all clauses of Sub Section General:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                update_all_section_one_general_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UPDATE_ALL_TDS_BTN)))
                update_all_section_one_general_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Closing Popup notification:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH)))
                popup_ok_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Go back to Tender Documents Dashboard:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                goto_tds_dashboard_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.GO_BACK_TO_TDS_DASHBOARD_BTN)))
                goto_tds_dashboard_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                

                # Sub Section B. e-Tender Document (e-TD)
                # =======================================
                # Clicking on Edit Button:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                edit_section_two_etd_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_TWO_ETENDER_DOCUMENT_EDIT_BTN)))
                edit_section_two_etd_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Insert e-Tender Document.
                etender_document_table  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_TWO_ETENDER_DOCUMENT_TDS_TABLE)))
                rows = etender_document_table.find_elements(By.TAG_NAME, "tr")

                for index, row in enumerate(rows):

                    if(row.text.find("10.2 A prospective Tenderer requiring any clarification"))>-1:
                        
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        etender_document_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(etender_document_iframe)

                        etender_document_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        etender_document_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.clarify_etd+"';", etender_document_body)

                        self.driver.switch_to.default_content()

                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("11.1 To clarify issues and to answer questions"))>-1:
                        
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        pretender_meeting_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(pretender_meeting_iframe)

                        pretender_meeting_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        pretender_meeting_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.pretender_meeting+"';", pretender_meeting_body)

                        self.driver.switch_to.default_content()

                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("11.2 Pre-Tender Meeting will be held online on the date"))>-1:
                        
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        pretender_meeting_time_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")

                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(pretender_meeting_time_iframe)

                        pretender_meeting_time_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        pretender_meeting_time_body.clear()

                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.pretender_meeting_time+"';", pretender_meeting_time_body)

                        self.driver.switch_to.default_content()

                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                # Clicking on Update all clauses of Sub Section General:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                update_all_section_two_etd_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UPDATE_ALL_TDS_BTN)))
                update_all_section_two_etd_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Closing Popup notification:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH)))
                popup_ok_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Go back to Tender Documents Dashboard:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                goto_tds_dashboard_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.GO_BACK_TO_TDS_DASHBOARD_BTN)))
                goto_tds_dashboard_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                

                # Sub Section C. Qualification Criteria
                # =======================================
                # Clicking on Edit Button:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                edit_section_three_qualification_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_THREE_QUALIFICATION_EDIT_BTN)))
                edit_section_three_qualification_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Insert e-Tender Document.
                qualification_criteria_table  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_THREE_QUALIFICATION_TDS_TABLE)))
                rows = qualification_criteria_table.find_elements(By.TAG_NAME, "tr")

                for index, row in enumerate(rows):

                    if(row.text.find("15.1 Tenderer shall have the following minimum level of construction experience"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        similar_experience_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(similar_experience_iframe)
                        similar_experience_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        similar_experience_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.similar_experience+"';", similar_experience_body)
                        self.driver.switch_to.default_content()
                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("(a) the average annual construction turnover"))>-1 and (row.text.find("(b) Availability of minimum liquid assets"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        turnover_and_liquid_asset_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(turnover_and_liquid_asset_iframe)
                        turnover_and_liquid_asset_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        turnover_and_liquid_asset_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.turnover+tender_datasheet.liquid_asset+"';", turnover_and_liquid_asset_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("(d) The Minimum Tender Capacity"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        tender_capacity_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(tender_capacity_iframe)
                        tender_capacity_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        tender_capacity_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.tender_capacity+"';", tender_capacity_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("17.1 Tenderer shall have the minimum level of personnel capacity"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        personnel_capacity_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(personnel_capacity_iframe)
                        personnel_capacity_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        personnel_capacity_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.personnel_capacity+"';", personnel_capacity_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("18.1 Tenderer shall own suitable equipment and other physical facilities"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        equipment_capacity_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(equipment_capacity_iframe)
                        equipment_capacity_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        equipment_capacity_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.equipment_capacity+"';", equipment_capacity_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("19.1 Tenderer may participate in the procurement proceedings forming a Joint Venture"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        jvca_criteria_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(jvca_criteria_iframe)
                        jvca_criteria_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        jvca_criteria_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.jvca+"';", jvca_criteria_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("19.2 The figures for each of the partners of a JVCA"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        jvca_clause_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(jvca_clause_iframe)
                        jvca_clause_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        jvca_clause_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.jvca_clause+"';", jvca_clause_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("20.3 PE may also select nominated Subcontractor(s)"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        subcontract_info_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(subcontract_info_iframe)
                        subcontract_info_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        subcontract_info_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.subcontract_info+"';", subcontract_info_body)
                        self.driver.switch_to.default_content()
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                # Clicking on Update all clauses of Sub Section General:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                update_all_section_three_qualification_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UPDATE_ALL_TDS_BTN)))
                update_all_section_three_qualification_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Closing Popup notification:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH)))
                popup_ok_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Go back to Tender Documents Dashboard:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                goto_tds_dashboard_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.GO_BACK_TO_TDS_DASHBOARD_BTN)))
                goto_tds_dashboard_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                


                # Sub Section D. Tender Preparation
                # =======================================
                # Clicking on Edit Button:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                edit_section_four_tender_prep_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_FOUR_TENDER_PREP_EDIT_BTN)))
                edit_section_four_tender_prep_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Insert e-Tender Document.
                tender_prep_table  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_FOUR_TENDER_PREP_TDS_TABLE)))
                rows = tender_prep_table.find_elements(By.TAG_NAME, "tr")

                for index, row in enumerate(rows):

                    if(row.text.find("25.1 The Tender prepared by the Tenderer shall comprise the following"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        additional_documents_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(additional_documents_iframe)
                        additional_documents_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        additional_documents_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.additional_docs+"';", additional_documents_body)
                        self.driver.switch_to.default_content()
                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                    if(row.text.find("26.3 Unless otherwise provided in the TDS and the Contract, the price"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        price_adjustment_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(price_adjustment_iframe)
                        price_adjustment_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        price_adjustment_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.price_adjuctment+"';", price_adjustment_body)
                        self.driver.switch_to.default_content()
                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                # Clicking on Update all clauses of Sub Section General:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                update_all_section_four_tender_prep_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UPDATE_ALL_TDS_BTN)))
                update_all_section_four_tender_prep_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Closing Popup notification:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH)))
                popup_ok_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                
                # Go back to Tender Documents Dashboard:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                goto_tds_dashboard_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.GO_BACK_TO_TDS_DASHBOARD_BTN)))
                goto_tds_dashboard_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                



                # Sub Section E. Tender e-Submission
                # =======================================
                # Clicking on Edit Button:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                edit_section_five_etender_submission_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_FIVE_ETENDER_SUBMISSION_EDIT_BTN)))
                edit_section_five_etender_submission_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Insert e-Tender Document.
                etender_submission_table  = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.SECTION_FIVE_ETENDER_SUBMISSION_TDS_TABLE)))
                rows = etender_submission_table.find_elements(By.TAG_NAME, "tr")

                for index, row in enumerate(rows):

                    if(row.text.find("40.1 e-Tenders shall be submitted to the e-GP System"))>-1:
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------
                        etender_submission_iframe  = rows[index+1].find_element(By.CSS_SELECTOR, "iframe")
                        # Switch to the iframe containing the CKEditor
                        self.driver.switch_to.frame(etender_submission_iframe)
                        etender_submission_body  = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        etender_submission_body.clear()
                        self.driver.execute_script("arguments[0].innerHTML = '"+tender_datasheet.submission_deadline+"';", etender_submission_body)
                        self.driver.switch_to.default_content()
                        # Wait until the page loading complete.
                        # ---------------------------------------------------------------------------------------------------------------
                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                        # ---------------------------------------------------------------------------------------------------------------

                # Clicking on Update all clauses of Sub Section General:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                update_all_section_five_etender_submission_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.UPDATE_ALL_TDS_BTN)))
                update_all_section_five_etender_submission_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                # Closing Popup notification:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                popup_ok_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.POPUP_OK_BTN_XPATH)))
                popup_ok_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                
                # Go back to Tender Documents Dashboard:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                goto_tds_dashboard_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.GO_BACK_TO_TDS_DASHBOARD_BTN)))
                goto_tds_dashboard_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------

                print("Successfully filled up Tender Document.")
                # '''
                # Go back to Tender/Proposal Document Preparation:
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                go_back_tender_prep_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.GO_BACK_TO_TENDER_PREPARATION_BTN)))
                go_back_tender_prep_btn.click()
                # ---------------------------------------------------------------------------------------------------------------
                self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                # ---------------------------------------------------------------------------------------------------------------
                
            
            else: 
                print (f"Standard Tender Document: {tender_datasheet.std_document} not found!")

            

        # except TimeoutException:
        except Exception:
            print("There is a Problem")


    def prepare_tender_document_pcc(self, tender_pcc):
        # try:
            # Particular Conditions of Contract
            # Clicking on Edit Button (PCC):
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            edit_tender_datasheet_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.PCC_EDIT_BTN)))
            edit_tender_datasheet_btn.click()
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            pcc_page_all_tables  = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))
            # print(pcc_page_all_tables.count)
            # retries = 0
            # while retries < pcc_page_all_tables.count:
            #     try:
            for pcc_table in pcc_page_all_tables:
                pcc_header = pcc_table.find_element(By.TAG_NAME, "tr")
                if(pcc_header.text.find("PCC Clause") !=-1 and pcc_header.text.find("PCC Clause") != -1):

                    retries = 30
                    for _ in range(retries):
                        try:
                            
                            pcc_table_rows = pcc_table.find_elements(By.TAG_NAME, "tr")
                            for index, pcc_table_row in enumerate(pcc_table_rows):

                                # print(f"{index}+++{pcc_table_row.text}")

                                if(pcc_table_row.text.find("40.1 Except otherwise specified in the PCC , the Commencement Date"))!=-1:
                                    # print(f"{index+3}---{pcc_table_rows[index+3].text}")
                                    if pcc_table_rows[index+3].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        print("Inserting Commencement Date")
                                        commencement_date_add_btn = pcc_table_rows[index+3].find_element(By.TAG_NAME, "a")
                                        commencement_date_add_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        
                                        commencement_date_inputbox = pcc_table_rows[index+5].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        
                                        self.driver.execute_script("arguments[0].removeAttribute('readonly')", commencement_date_inputbox)
                                        commencement_date_inputbox.clear()
                                        commencement_date_inputbox.send_keys(tender_pcc.work_start_date)
                                        self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", commencement_date_inputbox)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_commencement_date_btn = pcc_table_rows[index+6].find_element(By.TAG_NAME, "input")
                                        save_commencement_date_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                            for index, pcc_table_row in enumerate(pcc_table_rows):

                                # print(f"{index}==={pcc_table_row.text}")

                                if(pcc_table_row.text.find("(y) Intended Completion Date is the date calculated from the Commencement Date"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        print("Intended Completion Days")
                                        completion_duration_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        completion_duration_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        completion_duration_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        completion_duration_inputbox.clear()
                                        completion_duration_inputbox.send_keys(tender_pcc.days_to_complete)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_completion_duration_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_completion_duration_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("(kk) Site means the places where the Permanent Works are to be executed"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        site_location_and_drawing_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        site_location_and_drawing_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        site_location_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "textarea")
                                        site_location_inputbox.clear()
                                        site_location_inputbox.send_keys(tender_pcc.site_location)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        drawing_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[2].find_element(By.TAG_NAME, "textarea")
                                        drawing_inputbox.clear()
                                        drawing_inputbox.send_keys(tender_pcc.drawings_no)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_location_and_drawing_btn = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_location_and_drawing_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------

                                if(pcc_table_row.text.find("(nn) Start Date is the date defined in the PCC"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_start_limit_days_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        work_start_limit_days_add_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_start_limit_days_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        work_start_limit_days_inputbox.clear()
                                        work_start_limit_days_inputbox.send_keys(tender_pcc.days_to_start_work)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_work_start_limit_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_work_start_limit_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------

                                
                                if(pcc_table_row.text.find("(rr) Works means all works associated with the construction, reconstruction"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_component_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        work_component_add_btn.click()
                                        print("Work component info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_component_inputbox = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "textarea")
                                        work_component_inputbox.clear()
                                        work_component_inputbox.send_keys(tender_pcc.work_summary)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_work_component_btn = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_work_component_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                

                                
                                if(pcc_table_row.text.find("j. any other document listed in the PCC forming part of the Contract."))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        other_document_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        other_document_add_btn.click()
                                        print("Other documents requirement info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        other_document_inputbox = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "textarea")
                                        other_document_inputbox.clear()
                                        other_document_inputbox.send_keys(tender_pcc.other_documents)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_other_document_btn = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_other_document_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                            


                                
                                if(pcc_table_row.text.find("9.1 The Contractor and its Subcontractor(s) shall have the nationality"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        eligible_country_pcc_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        eligible_country_pcc_add_btn.click()
                                        print("Eligible Country info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        eligible_country_pcc_inputbox = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "textarea")
                                        eligible_country_pcc_inputbox.clear()
                                        eligible_country_pcc_inputbox.send_keys(tender_pcc.eligible_country_pcc)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_eligible_country_pcc_btn = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_eligible_country_pcc_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                


                                
                                if(pcc_table_row.text.find("9.2 All materials, equipment, plant, and supplies used by the Contractor"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        eligible_materials_pcc_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        eligible_materials_pcc_add_btn.click()
                                        print("Eligible Country of Origin info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        eligible_materials_pcc_inputbox = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "textarea")
                                        eligible_materials_pcc_inputbox.clear() 
                                        eligible_materials_pcc_inputbox.send_keys(tender_pcc.eligible_materials_pcc)
                                        # eligible_materials_pcc_inputbox = None
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_eligible_materials_pcc_btn = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_eligible_materials_pcc_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                

                                if(pcc_table_row.text.find("13.1 The PE shall give possession of the Site or part(s) of the Site, to the Contractor on the date(s) stated in the PCC."))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        site_possession_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        site_possession_add_btn.click()
                                        print("Site Possession Info and Date")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        site_possession_inputbox = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "textarea")
                                        site_possession_inputbox.clear() 
                                        site_possession_inputbox.send_keys(tender_pcc.site_possession)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        site_possession_date_inputbox =  pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[3].find_element(By.TAG_NAME, "input")
                                        self.driver.execute_script("arguments[0].removeAttribute('readonly')", site_possession_date_inputbox)
                                        site_possession_date_inputbox.clear()
                                        site_possession_date_inputbox.send_keys(tender_pcc.site_possession_date)
                                        self.driver.execute_script("arguments[0].setAttribute('readonly', 'true')", site_possession_date_inputbox)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_site_possession_btn = pcc_table_rows[index+4].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_site_possession_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                
    
                                if(pcc_table_row.text.find("42.1 Within the time stated in the PCC, the Contractor shall submit to the Project Manager for approval a Programme of Works"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_programme_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        work_programme_add_btn.click()
                                        print("Programme of Works info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_programme_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        work_programme_inputbox.clear()
                                        work_programme_inputbox.send_keys(tender_pcc.days_to_submit_work_programme)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_work_programme_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_work_programme_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("42.2 The Contractor shall submit to the Project Manager for approval of an updated Programme"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_programme_update_interval_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        work_programme_update_interval_add_btn.click()
                                        print("Update Programme of Works info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_programme_update_interval_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        work_programme_update_interval_inputbox.clear()
                                        work_programme_update_interval_inputbox.send_keys(tender_pcc.work_prog_update_days)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_work_programme_update_interval_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_work_programme_update_interval_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("42.3 If the Contractor does not submit an updated Programme of Works"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_programme_late_fee_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        work_programme_late_fee_add_btn.click()
                                        print("Late Submission fee")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        work_programme_late_fee_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        work_programme_late_fee_inputbox.clear()
                                        work_programme_late_fee_inputbox.send_keys(tender_pcc.work_prog_late_submn_fee)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_work_programme_late_fee_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_work_programme_late_fee_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("57.1 The Project Manager shall give notice to the Contractor, with a copy to the PE"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        defect_liability_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        defect_liability_add_btn.click()
                                        print("Defect Liability Period")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        defect_liability_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        defect_liability_inputbox.clear()
                                        defect_liability_inputbox.send_keys(tender_pcc.defect_liability_months)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_defect_liability_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_defect_liability_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("71.1 Prices shall be adjusted for fluctuations in the cost of inputs only if provided for in the PCC."))!=-1: 
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        price_adjustment_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        price_adjustment_add_btn.click()
                                        print("Price adjustment")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        price_adjustment_dropdown = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "select")
                                        price_adjustment_select = Select(price_adjustment_dropdown)
                                        price_adjustment_select.select_by_visible_text(tender_pcc.price_adjustment)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_price_adjustment_btn = pcc_table_rows[index+6].find_element(By.TAG_NAME, "input")
                                        save_price_adjustment_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("72.1 The PE may retain from each progressive payment due to the Contractor"))!=-1: 
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        performance_security_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        performance_security_add_btn.click()
                                        print("Performance Security info.")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        performance_security_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        performance_security_inputbox.clear()
                                        performance_security_inputbox.send_keys(tender_pcc.performance_security)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_performance_security_btn = pcc_table_rows[index+5].find_element(By.TAG_NAME, "input")
                                        save_performance_security_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("73.1 The Contractor shall pay liquidated damages to the PE at the rate per day stated in the PCC"))!=-1: 
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        liquidated_damage_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        liquidated_damage_add_btn.click()
                                        print("Liquidated Damages info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        liquidated_damage_per_day_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[0].find_element(By.TAG_NAME, "input")
                                        liquidated_damage_per_day_inputbox.clear() 
                                        liquidated_damage_per_day_inputbox.send_keys(tender_pcc.liquid_damage_per_day)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        liquidated_damage_max_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        liquidated_damage_max_inputbox.clear() 
                                        liquidated_damage_max_inputbox.send_keys(tender_pcc.liquid_damage_max)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_liquidated_damage_btn = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_liquidated_damage_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("75.1 If so specified in the PCC, the PE shall make advance payment to the Contractor"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        advanced_payment_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        advanced_payment_add_btn.click()
                                        print("Advance Payment")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        advanced_payment_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[0].find_element(By.TAG_NAME, "input")
                                        advanced_payment_inputbox.clear() 
                                        advanced_payment_inputbox.send_keys(tender_pcc.advance_amount)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_advanced_payment_btn = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_advanced_payment_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("84.1 If “As Built” Drawings and/or operating and maintenance manuals are required"))!=-1: 
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        as_built_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        as_built_add_btn.click()
                                        print("As-built Drawings and Manuals")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        as_built_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[0].find_element(By.TAG_NAME, "input")
                                        as_built_inputbox.clear() 
                                        as_built_inputbox.send_keys(tender_pcc.as_built_drawing_days)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        onm_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        onm_inputbox.clear() 
                                        onm_inputbox.send_keys(tender_pcc.onm_days)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_as_built_btn = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[2].find_element(By.TAG_NAME, "input")
                                        save_as_built_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("84.2 If the Contractor does not supply the Drawings and/or Manuals by the dates specified in GCC"))!=-1: 
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        as_built_late_fee_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        as_built_late_fee_add_btn.click()
                                        print("As-Built Drawing late fee")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        as_built_late_fee_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        as_built_late_fee_inputbox.clear()
                                        as_built_late_fee_inputbox.send_keys(tender_pcc.as_built_drawing_late_fee)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_as_built_late_fee_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_as_built_late_fee_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------


                                if(pcc_table_row.text.find("90.1 If the Contract is terminated because of a fundamental breach of Contract"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        termination_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        termination_add_btn.click()
                                        print("Payment upon Termination")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        termination_inputbox = pcc_table_rows[index+3].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "input")
                                        termination_inputbox.clear()
                                        termination_inputbox.send_keys(tender_pcc.termination_payment_percent)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_termination_btn = pcc_table_rows[index+4].find_element(By.TAG_NAME, "input")
                                        save_termination_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------

                                
                                if(pcc_table_row.text.find("94.2 Adjudication"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        adjudication_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        adjudication_add_btn.click()
                                        print("Adjudication Info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        adjud_name_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[0].find_element(By.TAG_NAME, "textarea")
                                        adjud_name_inputbox.clear() 
                                        adjud_name_inputbox.send_keys(tender_pcc.adjud_name)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        adjud_address_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "textarea")
                                        adjud_address_inputbox.clear() 
                                        adjud_address_inputbox.send_keys(tender_pcc.adjud_address)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        adjud_phone_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[2].find_element(By.TAG_NAME, "input")
                                        adjud_phone_inputbox.clear() 
                                        adjud_phone_inputbox.send_keys(tender_pcc.adjud_phone)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        adjud_fax_inputbox = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")[3].find_element(By.TAG_NAME, "input")
                                        adjud_fax_inputbox.clear() 
                                        adjud_fax_inputbox.send_keys(tender_pcc.adjud_fax)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_adjudication_btn = pcc_table_rows[index+3].find_element(By.CSS_SELECTOR, "tbody").find_elements(By.TAG_NAME, "tr")[3].find_element(By.TAG_NAME, "input")
                                        save_adjudication_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------

                                
                                if(pcc_table_row.text.find("94.3 Arbitration"))!=-1:
                                    if pcc_table_rows[index+1].find_element(By.TAG_NAME, "a").text.find("Add") !=-1:
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        arbitration_add_btn = pcc_table_rows[index+1].find_element(By.TAG_NAME, "a")
                                        arbitration_add_btn.click()
                                        print("Arbitration Info")
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        rbitration_inputbox = pcc_table_rows[index+4].find_element(By.TAG_NAME, "textarea")
                                        rbitration_inputbox.clear() 
                                        rbitration_inputbox.send_keys(tender_pcc.arbitration_place)
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------
                                        save_arbitration_btn = pcc_table_rows[index+5].find_element(By.TAG_NAME, "input")
                                        save_arbitration_btn.click()
                                        # ---------------------------------------------------------------------------------------------------------------
                                        self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
                                        # ---------------------------------------------------------------------------------------------------------------

                            break
                        
                        except:
                            time.sleep(5)
                    else:
                        print("Failed to find element after {} retries.".format(retries))
                   

    #Function for Downloading Documents just after Opening of the tender.   
    def download_documents_for_evaluation (self, tender_id):

        default_download_folder =  os.path.join(os.path.expanduser("~"),"Downloads")
        tender_directory = os.path.join(os.getcwd(), tender_id)



        try:
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            # Navigating to Opening Tab:
            tender_opening_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_OPENING_OTHER_TAB)))
            tender_opening_tab.click()
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            tenderer_info_part_one = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDERER_INFO_PART_ONE)))
            tenderer_info_part_one.click()
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            individual_report_tables  = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,EgpXpaths.PART_TWO_TABLES_XPATH))) 
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            for counter, table in enumerate(individual_report_tables):

                if(counter>1 and counter%2==0):
                    download_dir = os.path.join(tender_directory, table.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(4) > td > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)").text.replace("/", "").replace("\\", ""), "Part-1")
                    os.makedirs(download_dir, exist_ok=True)

                elif(counter>1 and counter%2==1):
                    mapped_doc_list = table.find_elements(By.TAG_NAME, "tr")
                    for document_row in mapped_doc_list:
                        try:
                            download_btn = document_row.find_element(By.CLASS_NAME, 'action-button-download')
                            sl_no = document_row.find_element(By.TAG_NAME, 'td')
                            download_btn.click()

                            Utility.file_downloader(default_download_folder, download_dir, sl_no.text)
                            
                        except NoSuchElementException:
                            print(">>")
            
            


            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            go_back_opening_page = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDER_INFO_BACK_BTN)))
            go_back_opening_page.click()
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            
            tenderer_info_part_two = self.wait.until(EC.presence_of_element_located((By.XPATH, EgpXpaths.TENDERER_INFO_PART_TWO)))
            tenderer_info_part_two.click()
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------
            individual_report_tables  = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,EgpXpaths.PART_TWO_TABLES_XPATH))) 
            # ---------------------------------------------------------------------------------------------------------------
            self.wait.until(lambda x: x.execute_script("return (document.readyState === 'complete' && jQuery.active === 0)"))
            # ---------------------------------------------------------------------------------------------------------------

            for counter, table in enumerate(individual_report_tables):

                if(counter>1 and counter%2==0):
                    download_dir = os.path.join(tender_directory, table.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(4) > td > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)").text.replace("/", "").replace("\\", ""), "Part-2")
                    os.makedirs(download_dir, exist_ok=True)

                elif(counter>1 and counter%2==1):
                    mapped_doc_list = table.find_elements(By.TAG_NAME, "tr")
                    for document_row in mapped_doc_list:
                        try:
                            download_btn = document_row.find_element(By.CLASS_NAME, 'action-button-download')
                            sl_no = document_row.find_element(By.TAG_NAME, 'td')
                            download_btn.click()

                            Utility.file_downloader(default_download_folder, download_dir, sl_no.text)
                            
                        except NoSuchElementException:
                            print(">>")


        except Exception as e:
            # print(f"Error Occured: {e}")
            print(f"{e}")
            return False
            

    def quit(self):
        self.driver.quit()




class PackageDetails:
    def __init__(self, pkg_no, pkg_name, location, budget, estimated_cost, quantity, unit):
        self.pkg_no = pkg_no
        self.pkg_name = pkg_name
        self.location = location
        self.budget = budget
        self.estimated_cost = estimated_cost
        self.quantity = quantity
        self.unit = unit

class AppPackage:
    def __init__(self, financial_year, budget_type, approval_status, app_id, tender_type, 
                 procur_nature, emrgency, app_cost, approv_authority, procure_type, 
                 procure_method, exp_ift_dt, submsn_duration, opening_duration, eval_submn_duration,
                 contract_aproval_duration, noa_duration, contr_sign_durataion, contr_comp_duration):
        self.financial_year = financial_year
        self.budget_type = budget_type
        self.approval_status = approval_status
        self.app_id = app_id
        self.tender_type = tender_type
        self.procur_nature = procur_nature
        self.emrgency = emrgency
        self.app_cost = app_cost
        self.approv_authority = approv_authority
        self.procure_type = procure_type
        self.procure_method = procure_method
        self.exp_ift_dt = exp_ift_dt
        self.submsn_duration = submsn_duration
        self.opening_duration = opening_duration
        self.eval_submn_duration = eval_submn_duration
        self.contract_aproval_duration = contract_aproval_duration
        self.noa_duration = noa_duration
        self.contr_sign_durataion = contr_sign_durataion
        self.contr_comp_duration = contr_comp_duration

class TenderNotice:
    def __init__(self, notice_memo_date, publish_datetime, last_sell_datetime, meeting_start_datetime,
                 meeting_end_datetime, closing_datetime, security_subnm_datetime, eligibility, brief_desc, tender_security_bdt,
                 work_start_date, work_end_date, approving_authority, standard_document, tender_validity):
        self.notice_memo_date = notice_memo_date
        self.publish_datetime = publish_datetime
        self.last_sell_datetime = last_sell_datetime
        self.meeting_start_datetime = meeting_start_datetime
        self.meeting_end_datetime = meeting_end_datetime
        self.closing_datetime = closing_datetime
        self.security_subnm_datetime = security_subnm_datetime
        self.eligibility = eligibility
        self.brief_desc = brief_desc
        self.tender_security_bdt = tender_security_bdt
        self.work_start_date = work_start_date
        self.work_end_date = work_end_date
        self.approving_authority = approving_authority
        self.standard_document = standard_document
        self.tender_validity = tender_validity

class TenderDataSheet:
    def __init__(self, std_document, general_info, fund_source, dev_partner, eligible_country,
                 eligible_materials, clarify_etd, pretender_meeting, pretender_meeting_time, similar_experience, turnover,
                 liquid_asset, tender_capacity, personnel_capacity, equipment_capacity, jvca, jvca_clause, subcontract_info,
                 additional_docs, price_adjuctment, submission_deadline):
        self.std_document = std_document
        self.general_info = general_info
        self.fund_source = fund_source
        self.dev_partner = dev_partner
        self.eligible_country = eligible_country
        self.eligible_materials = eligible_materials
        self.clarify_etd = clarify_etd
        self.pretender_meeting = pretender_meeting
        self.pretender_meeting_time = pretender_meeting_time
        self.similar_experience = similar_experience
        self.turnover = turnover
        self.liquid_asset = liquid_asset
        self.tender_capacity = tender_capacity
        self.personnel_capacity = personnel_capacity
        self.equipment_capacity = equipment_capacity
        self.jvca = jvca
        self.jvca_clause = jvca_clause
        self.subcontract_info = subcontract_info
        self.additional_docs = additional_docs
        self.price_adjuctment = price_adjuctment
        self.submission_deadline = submission_deadline

class TenderPCC:
    def __init__(self, work_start_date, days_to_complete, site_location, drawings_no, days_to_start_work,
                 site_possession_date, work_summary, other_documents, eligible_country_pcc, eligible_materials_pcc,
                 site_possession, days_to_submit_work_programme, work_prog_update_days, work_prog_late_submn_fee,
                 defect_liability_months, price_adjustment, performance_security, liquid_damage_per_day,
                 liquid_damage_max, advance_amount, as_built_drawing_days, onm_days, as_built_drawing_late_fee,
                 termination_payment_percent, adjud_name, adjud_address, adjud_phone, adjud_fax, arbitration_place):
        self.work_start_date = work_start_date
        self.days_to_complete = days_to_complete
        self.site_location = site_location
        self.drawings_no = drawings_no
        self.days_to_start_work = days_to_start_work
        self.site_possession_date = site_possession_date
        self.work_summary = work_summary
        self.other_documents = other_documents
        self.eligible_country_pcc = eligible_country_pcc
        self.eligible_materials_pcc = eligible_materials_pcc
        self.site_possession = site_possession
        self.days_to_submit_work_programme = days_to_submit_work_programme
        self.work_prog_update_days = work_prog_update_days
        self.work_prog_late_submn_fee = work_prog_late_submn_fee
        self.defect_liability_months = defect_liability_months
        self.price_adjustment = price_adjustment
        self.performance_security = performance_security
        self.liquid_damage_per_day = liquid_damage_per_day
        self.liquid_damage_max = liquid_damage_max
        self.advance_amount = advance_amount
        self.as_built_drawing_days = as_built_drawing_days
        self.onm_days = onm_days
        self.as_built_drawing_late_fee = as_built_drawing_late_fee
        self.termination_payment_percent = termination_payment_percent
        self.adjud_name = adjud_name
        self.adjud_address = adjud_address
        self.adjud_phone = adjud_phone
        self.adjud_fax = adjud_fax
        self.arbitration_place = arbitration_place