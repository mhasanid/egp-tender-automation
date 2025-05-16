class EgpXpaths:
    #Login XPATHs
    LOGIN_BTN_XPATH = "//*[@id='btnLogin']"
    EMAIL_INPUT_XPATH = "//input[@id='txtEmailId']"
    PASSWORD_INPUT_XPATH = "//input[@id='txtPassword']"

    # Popup windows button Xpaths
    POPUP_OK_BTN_XPATH = "//*[@id='popup_ok']"
    UPDATE_LATER_BTN_XPATH = "//*[@id='btnUpdateLater']"
    
    # APP Main Menu and Submenu Xpaths
    APP_MENU_XPATH = "//*[@id='headTabApp']" 
    MYAPP_SUBMENU_XPATH = "//*[@id='submenu-configuration']/li[2]/a"
    CREATE_APP_SUBMENU_XPATH = "//*[@id='submenu-configuration']/li[1]/a"

    # Create APP Xpaths:
    CREATE_APP_BUDGET_TYPE_XPATH = "//*[@id='cmbBudgetType']"
    CREATE_APP_FY_XPATH = "//*[@id='cmbFinancialYear']"
    CREATE_APP_CODE_XPATH = "//*[@id='txtAppCode']"
    CREATE_APP_NEXT_BTN_XPATH = "//*[@id='buttonNext']"
    CREATE_APP_ERROR_PLACEHOLDER_XPATH = "/html/body/div/div/table[1]/tbody/tr/td/div[2]"
    

    # MY APP Search Criteria XPATHs:
    MYAPP_FY_XPATH = "//*[@id='cmbFinancialYear']"
    MYAPP_BUDGET_TYPE_XPATH = "//*[@id='cmbbudgetType']"
    MYAPP_STATUS_XPATH = "//*[@id='cmbstatus']"
    MYAPP_APP_ID_XPATH = "//*[@id='txtAppId']" 
    APP_SEARCH_BTN_XPATH = "//*[@id='btnSearchApp']"
    APP_SEARCH_RESULT_TABLE_XPATH = "//*[@id='list']"
    ADD_NEW_PKG_BTN_XPATH = "/html/body/div/div/table[1]/tbody/tr/td/table/tbody/tr/td/div[2]/a[2]"
    
    #Add APP Packge Page: Xpaths of element:
    APP_ADD_PKG_APP_ID = "//*[@id='frmAddPackageDetail']/table/tbody/tr[2]/td[2]"
    APP_ADD_PKG_PKG_TYPE = "//*[@id='cmbAppType']"
    APP_ADD_PKG_PROCUR_NATURE = "//*[@id='cmbProcureNature']"
    APP_ADD_PKG_EMERGENCY_TYPE = "//*[@id='cmbEmergencyType']"
    APP_ADD_PKG_PKG_NO = "//*[@id='txtPackageNo']"
    APP_ADD_PKG_PKG_NO_MSG="//*[@id='pkgnoMsg']"
    APP_ADD_PKG_PKG_DESCRIPTION = "//*[@id='txtaPackageDesc']"
    APP_ADD_PKG_LOT_NO = "//*[@id='txtLotNo_1']"
    APP_ADD_PKG_LOT_DESCRIPTION = "//*[@id='txtLotDesc_1']"
    APP_ADD_PKG_QUANTITY = "//*[@id='txtQuantity_1']"
    APP_ADD_PKG_UNIT = "//*[@id='txtUnit_1']"
    APP_ADD_PKG_EST_COST = "//*[@id='txtEstimateCost_1']"
    APP_ADD_PKG_SELECT_CATEGORIES = "//*[@id='hrefCPV']"
    APP_ADD_PKG_APPROVING_AUTHORITY = "//*[@id='cmbAuthority']"
    APP_ADD_PKG_PQ_REQUIRES = "//*[@id='cmbPQRequires']"
    APP_ADD_PKG_PROCUR_TYPE = "//*[@id='cmbProcureType']"
    APP_ADD_PKG_PROCURE_METHOD = "//*[@id='cmbProcureMethod']"
    APP_ADD_PKG_NEXT_BTN = "//*[@id='btnNext']"

    APP_ADD_PKG_CATEGORY_CONSTR_WORK_TREE = "//*[@id='5815']/ins"
    APP_ADD_PKG_CATEGORY_CIVIL_WORK_TREE = "//*[@id='5867']/ins"
    APP_ADD_PKG_CATEGORY_WATER_PROJECT_TREE = "//*[@id='6260']/a/ins[1]"
    APP_ADD_PKG_CATEGORY_SUBMIT_BTN = "//*[@id='btnGetCheckedNode']"
    
    APP_ADD_PKG_EXPECTED_EGP_IFT_DATEPICKER = "//*[@id='txtRfqdtadvtift']"
    # APP_ADD_PKG_EXPECTED_EGP_IFT_DATEPICKER = "//*[@id='txtRfqdtadvtiftimg']"
    # APP_ADD_PKG_EXPECTED_EGP_IFT_DATEPICKER = "/html/body/table[2]/tbody/tr/td/div/div[1]/table/tbody/tr/td/div"
    APP_ADD_PKG_EXPECTED_LAST_SUBMISSION_INPUT = "//*[@id='txtRfqdtadvtiftNo']"
    APP_ADD_PKG_EXPECTED_OPENING_INPUT = "//*[@id='txtRfqdtsubNo']"
    APP_ADD_PKG_EXPECTED_EVALUATION_SUB_INPUT = "//*[@id='txtRfqexpdtopenNo']"
    APP_ADD_PKG_EXPECTED_APPROVAL_INPUT = "//*[@id='txtRfqdtsubevaRptNo']"
    APP_ADD_PKG_EXPECTED_NOA_ISSUE_INPUT = "//*[@id='txtRfqexpdtAppawdNo']"
    APP_ADD_PKG_EXPECTED_CONTRACT_SIGNING_INPUT = "//*[@id='txtRfqdtIssNOANo']"
    APP_ADD_PKG_EXPECTED_WORK_COMPLETION_DURATION_INPUT = "//*[@id='txtRfqexpdtSignNo']"

    APP_ADD_PKG_SAVE = "//*[@id='btnSave']"
    APP_PKGS_LIST_TABLE = "//*[@id='resultTable']"

    # Tender Main Menu and Submenu Xpaths
    TENDER_MENU_XPATH = "//*[@id='headTabTender']"  
    MY_TENDER_SUBMENU_PE_XPATH =  "//*[@id='ddsubmenu2']/li[2]/a"
    MY_TENDER_SUBMENU_OTHER_XPATH =  "//*[@id='ddsubmenu2']/li[1]/a"
    UNDER_PREPARATION_TAB = "//*[@id='pendingTab']"
    LIVE_TAB = "//*[@id='liveTab']"
    PROCESSING_TAB = "//*[@id='processingTab']"
    ARCHIVED_TAB = "//*[@id='archivedTab']"
    

    TENDER_ID_INPUT= "//*[@id='tenderId']"

    TENDER_SEARCH_RESULT_TABLE = "//*[@id='resultTable']/tbody"


    # Inside a Package-Payment Details:
    PAYMENT_BTN = "//*[@id='tabPayment']"
    PERFORMANCE_SECURITY_BTN = "/html/body/div/div[3]/div[4]/div[1]/ul/li[3]/a"
    VIEW_PERFORMANCE_BTN = "/html/body/div/div[3]/div[4]/table/tbody/tr[2]/td[3]/a"
    PERFORMANCE_PAYMENT_DETAILS_BY_CONTRACTOR_BTN = "/html/body/div/div[3]/table[2]/tbody/tr[2]/td[4]/a"
    TENDER_ID_LABEL = "//*[@id='resultDiv']/table/tbody/tr[1]/td[2]"
    PERFORMANCE_PAYMENT_DETAILS_TABLE = "//*[@id='print_area']/div[2]/table/tbody"


    # Tender Preparation
    TENDER_NOTICE_TAB = "//*[@id='offTabPanel']/li[1]/a"
    
    TENDER_EVALUATION_TAB = "//*[@id='offTabPanel']/li[3]/a"
    TENDER_OPENING_TAB = "//*[@id='offTabPanel']/li[4]/a"

    TENDER_OPENING_OTHER_TAB = "//*[@id='offTabPanel']/li[6]/a"

    
    # Tender Preparation Dashboard.
    #------------------------------------------------
    TENDER_NOTICE_EDIT_BTN= "/html/body/div[3]/div[4]/table[1]/tbody/tr[1]/td[2]/a[1]" 
    
    # Under Notice button the following form is to be filled up: 
    INVITATION_REFERENCE_NO_INPUT = "//*[@id='txtinvitationRefNo']"
    TENDER_PUBLICATION_DATE_TIME_INPUT = "//*[@id='txttenderpublicationDate']"
    TENDER_LAST_SELLING_DATE_TIME_INPUT = "//*[@id='txttenderLastSellDate']"
    PRE_TENDER_MEETING_START_DATE_TIME_INPUT = "//*[@id='txtpreTenderMeetStartDate']"
    PRE_TENDER_MEETING_END_DATE_TIME_INPUT = "//*[@id='txtpreTenderMeetEndDate']"
    TENDER_CLOSING_DATE_TIME_INPUT = "//*[@id='txtpreQualCloseDate']"
    TENDER_OPENING_DATE_TIME_INPUT = "//*[@id='txtpreQualOpenDate']"
    TENDER_SECURITY_SUBMN_DATE_TIME_INPUT = "//*[@id='txtlastDateTenderSub']"
    # ELIGIBILITY_OF_TENDERER_TXTBOX = "//*[@title='Rich Text Editor, txtaeligibilityofTenderer']"
    # ELIGIBILITY_OF_TENDERER_TXTBOX = "//*[@id='cke_contents_txtaeligibilityofTenderer']"
    ELIGIBILITY_OF_TENDERER_TXTBOX = "//*[@id='cke_txtaeligibilityofTenderer']"
    # BRIEF_DESCRIP_OF_WORKS_TXTBOX = "//*[@title='Rich Text Editor, txtabriefDescGoods']"
    # BRIEF_DESCRIP_OF_WORKS_TXTBOX = "//*[@id='cke_contents_txtabriefDescGoods']"
    BRIEF_DESCRIP_OF_WORKS_TXTBOX = "//*[@id='cke_txtabriefDescGoods']"
    LOCATION_OF_WORK_INPUT = "//*[@id='locationlot_0']"
    TENDER_SECURITY_INPUT = "//*[@id='tenderSecurityAmount_0']"
    TENTATIVE_WORK_START_DATE_INPUT = "//*[@id='startTimeLotNo_0']"
    TENTATIVE_WORK_END_DATE_INPUT = "//*[@id='complTimeLotNo_0']"
    NOTICE_SUBMIT_BTN = "//*[@id='btnsubmit']"
    CONFIG_KEY_INFO_CREATE_BTN = "/html/body/div[3]/div[4]/table[1]/tbody/tr[2]/td[2]/a"
    CONFIG_KEY_INFO_EDIT_BTN = "/html/body/div[3]/div[4]/table[1]/tbody/tr[2]/td[2]/a[1]"

    # EXPAND_STD_BTN = "//*[@id='collSTD']"
    APPROVING_AUTHORITY_INPUT = "//*[@id='cmbappAuthority']"
    STANDARD_TENDER_DOCUMENT_INPUT = "//*[@id='tenderDocument']"

    TENDER_VALIDITY_DAYS_INPUT = "//*[@id='txttenderValidity']"
    #Tender/Proposal Security Validity In No. of Days = "//*[@id='txttenderSecurityValidity']"
    SUBMIT_STD_BTN = "//*[@id='btnSubmit']"
    # EXPAND_SECTION_BTN = "//*[@id='collSTDSec']"
    SAVE_FIRST_SECTION_BTN = "//*[@id='btnSubmitSection']"
    SAVE_SECOND_SECTION_BTN = "//*[@id='btnSubmitForm']"

    GO_BACK_TO_DASHBOARD_BTN ="/html/body/div/div[2]/div[1]/span/a"

    CLARIFICATION_TENDER_BTN = "/html/body/div[3]/div[4]/table[1]/tbody/tr[3]/td[2]/a"
    CLARIFICATION_TENDER_ALLOWED_INPUT = "//*[@id='claricomboid']"

    
    #----------------------------------------------------------
    TENDER_DOCUMENT_TAB = "//*[@id='offTabPanel']/li[2]/a"
    
    # FOR e-PW3
    # Tender Data Sheet
    TENDER_DATA_SHEET_EDIT_BTN = "/html/body/div/div[3]/div[4]/table[3]/tbody/tr[5]/td[3]/a[1]"

    UPDATE_ALL_TDS_BTN ="//*[@id='updateAllBottom']"
    GO_BACK_TO_TDS_DASHBOARD_BTN = "/html/body/div/div/table[1]/tbody/tr/td/table[1]/tbody/tr/td[2]/a"

    SECTION_ONE_GENERAL_EDIT_BTN = "/html/body/div/div/table[1]/tbody/tr/td/form/table/tbody/tr[3]/td[2]/a[1]"
    SECTION_ONE_GENERAL_TDS_TABLE = "//*[@id='tdsInfo']"
    
    SECTION_TWO_ETENDER_DOCUMENT_EDIT_BTN = "/html/body/div/div/table[1]/tbody/tr/td/form/table/tbody/tr[6]/td[2]/a[1]"
    SECTION_TWO_ETENDER_DOCUMENT_TDS_TABLE = "//*[@id='tdsInfo']"
    
    SECTION_THREE_QUALIFICATION_EDIT_BTN = "/html/body/div/div/table[1]/tbody/tr/td/form/table/tbody/tr[9]/td[2]/a[1]"
    SECTION_THREE_QUALIFICATION_TDS_TABLE= "//*[@id='tdsInfo']"

    SECTION_FOUR_TENDER_PREP_EDIT_BTN = "/html/body/div/div/table[1]/tbody/tr/td/form/table/tbody/tr[12]/td[2]/a[1]"
    SECTION_FOUR_TENDER_PREP_TDS_TABLE= "//*[@id='tdsInfo']"

    SECTION_FIVE_ETENDER_SUBMISSION_EDIT_BTN = "/html/body/div/div/table[1]/tbody/tr/td/form/table/tbody/tr[15]/td[2]/a[1]"
    SECTION_FIVE_ETENDER_SUBMISSION_TDS_TABLE= "//*[@id='tdsInfo']"

    GO_BACK_TO_TENDER_PREPARATION_BTN = "/html/body/div/div/table[1]/tbody/tr/td/div/div/span/a"
    
    # Particular Condition of Contract
    PCC_EDIT_BTN = "/html/body/div/div[3]/div[4]/table[3]/tbody/tr[7]/td[3]/a[1]"
    
    ACTIVITY_FORM_DASHBOARD = "/html/body/div/div[3]/div[4]/table[3]/tbody/tr[8]/td[2]/table[3]/tbody/tr[13]/td[3]/a[1]"
    ACTIVITY_TABLE_MATRIX_FILL_UP_BTN = "/html/body/div/div[3]/table[3]/tbody/tr[2]/td[2]/a[1]" 
    ACTIVITY_CSV_FILE_INPUT = "//*[@id='txtFile']"
    ACTIVITY_CSV_FILE_INPUT_SUBMIT_BTN = "//*[@id='submitID']"

    BOQ_DASHBOARD = "/html/body/div/div[3]/div[4]/table[3]/tbody/tr[9]/td[2]/table[5]/tbody/tr[2]/td[3]/a[2]"
    BOQ_TABLE_MATRIX_FILL_UP_BTN = "/html/body/div/div[3]/table[3]/tbody/tr[2]/td[2]/a[1]"
    BOQ_CSV_FILE_INPUT = "//*[@id='txtFile']"
    BOQ_CSV_FILE_INPUT_SUBMIT_BTN = "//*[@id='submitID']"


    # Tender Opening Committee
    PERSONNEL_INFO_LINK_XPATH = "/html/body/div[1]/div[3]/div[6]/table[4]/tbody/tr[9]/td[2]/a[2]"
    TENDERER_INFO_PART_ONE = "/html/body/div[1]/div[3]/div[6]/table[4]/tbody/tr[11]/td[2]/a[2]"
    TENDERER_INFO_PART_TWO = "/html/body/div[1]/div[3]/div[6]/table[4]/tbody/tr[12]/td[2]/a[2]"

    TENDER_INFO_BACK_BTN = "/html/body/div/div[2]/span/a[3]"  

    PART_TWO_TABLES_XPATH = "//*[@id='print_area']/table"


    # //*[@id="print_area"]/table[4]/tbody
    # //*[@id="print_area"]/table[6]/tbody

    # //*[@id="mtable1"]/tbody/tr[1]/td/b/center/a
    # //*[@id="mtable1"]/tbody/tr[1]/td/b/center
    

