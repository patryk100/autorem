import json

def analyze(evt):
    print("Analyzing")

def asff_format(evt):
    print("formatting")

def main():
    with open('events.json', 'r') as f:
        evt_data = json.load(f)
    print(json.dumps(evt_data, indent=2))

    evt_id = evt_data.get('Findings')[0].get('Id')
    print(f"Analyzing events: {evt_id}")
    analyze(evt_data)
    print(f"Formatting events: {evt_id}")
    asff_format(evt_data)




if __name__ == "__main__":
    main()


# Generates dummy findings in your actual AWS console
# aws guardduty list-detectors
# https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html
# aws guardduty create-sample-findings \
#     --detector-id <YOUR_DETECTOR_ID> \
#     --finding-types "PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated"
# filter.json
# {
#     "Criterion": {
#       "type": {
#         "Eq": [
#           "PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated"
#         ]
#       }
#     }
#   }
#
# aws guardduty list-findings --detector-id <YOUR_DETECTOR_ID> --finding-criteria file://filter.json --output json > findings_list.json
# aws guardduty get-findings --detector-id <YOUR_DETECTOR_ID> --finding-ids <ID_FROM_ABOVE> > events.json
