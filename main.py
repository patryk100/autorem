import json

def analyze(evt):
    # dynamically get this from evt
    return {
        "Name": "test",
        "Sev" :  9.9,
        "Type": "Ransomware"
    }


def asff_format(d, evt):
    print(f"{evt.get('Name')}")

def main():
    with open('events.json', 'r') as f:
        evt_data = json.load(f)
    # print(json.dumps(evt_data, indent=2))
    events = evt_data.get('findings'.title())
    for event in events:
        evt_id = event.get('Id')
        detection = analyze(evt_data)
        if not detection:
            print(f"Event: {evt_id} is clean")
        else:
            print(f"Threat detected in: {evt_id}")
            for d in detection:
                asff_evt = asff_format(d, event) # pass in analyze finidings, and event
                # auto remediate func
                # pass in asff evt
        print("********************************\n")



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
