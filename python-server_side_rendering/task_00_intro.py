#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees."""
    if not isinstance(template, str):
        print("Error: template is not a string")
        return
    if not isinstance(attendees, list) or not all(
            isinstance(a, dict) for a in attendees):
        print("Error: attendees is not a list of dictionaries")
        return
    if template == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    for i, attendee in enumerate(attendees, 1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))
        with open("output_{}.txt".format(i), "w") as f:
            f.write(output)
