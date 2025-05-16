from enum import Enum

class BudgetType(Enum):
    DEVELOPMENT = "Development Budget"
    REVENUE = "Revenue Budget"
    OWN = "Own Fund"

class TenderType(Enum):
    EGP = "e-GP"
    MANUAL = "Manual"

class ProcureNature(Enum):
    GOODS = "Goods"
    WORKS = "Works"
    SERVICES = "Services"

class EmergencyType(Enum):
    NORMAL = "Normal"
    URGENT = "Urgent(Catastrophe)"
    DISASTER = "National disaster"

class ApprovingAuthority(Enum):
    PE="PE"
    SECRETARY = "Secretary"
    MINISTER = "Minister"
    BOD = "BOD"
    HOPE = "HOPE"
    CCGP = "CCGP"
    AO = "AO"

class PostQualification(Enum):
    YES = "Yes"
    NO = "No"

class ProcureType(Enum):
    NCT = "NCT "
    ICT = "ICT"

class ProcureMethod(Enum):
    DPM = "Direct Procurement"
    LTM = "Limited Tendering Method"
    OSTEM = "One stage Two Envelopes Tendering Method"
    OTM = "Open Tendering Method"
    RFQ_LUMP_SUM = "Request For Quotation Lump Sum"
    RFQ_UNIT_RATE = "Request For Quotation Unit Rate"
    TSM = "Two Stage Tendering Method"