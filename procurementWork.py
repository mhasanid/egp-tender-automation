class ProcurementWork:
    def __init__(self, pkg_no, pkg_name, invitation_memo, location, estimated_cost):
        self.pkg_no = pkg_no
        self.pkg_name = pkg_name
        self.invitation_memo = invitation_memo
        self.location = location
        self.estimated_cost = estimated_cost

    def approving_authority(self, authority_level):
        return f"Approval granted by {authority_level} authority."

    def tender_floating_days(self, days):
        return f"Tender floating days set to {days} days."

work_instance = ProcurementWork(pkg_no=1, pkg_name="Example Package", invitation_memo="Memo content",
                                location="Example Location", estimated_cost=100000)

approval_message = work_instance.approving_authority("Senior Management")
floating_days_message = work_instance.tender_floating_days(30)

print(approval_message)
print(floating_days_message)