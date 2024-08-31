PROCESS_STEPS = [
    {
        "id": "1",
        "name": "Deal Done",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "1.1", "name": "Review of Cargo Nominations", "type": "sub", "highlighted": True},
            {"id": "1.2", "name": "Ship Adaptability", "type": "sub", "highlighted": False},
            {"id": "1.3", "name": "SAFE Acceptability", "type": "sub", "highlighted": True},
            {"id": "1.4", "name": "Previous Cargo?", "type": "sub", "highlighted": False},
            {"id": "1.5", "name": "Stowage Plan", "type": "sub", "highlighted": False},
            {"id": "1.6", "name": "STAR Risk Assessment", "type": "sub", "highlighted": True},
        ]
    },
    {
        "id": "2",
        "name": "Arrival at Loadport",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "2.1", "name": "Check DEX Entries and FED Contracts", "type": "sub", "highlighted": True},
            {"id": "2.2", "name": "Financial Securities", "type": "sub", "highlighted": False},
            {"id": "2.3", "name": "Identify Terms of Deals (CIF/FOB)", "type": "sub", "highlighted": True},
            {"id": "2.4", "name": "Assign Ship", "type": "sub", "highlighted": False},
            {"id": "2.5", "name": "Nominate to the Terminal", "type": "sub", "highlighted": False},
            {"id": "2.6", "name": "Update DEX & RADAR", "type": "sub", "highlighted": True},
            {"id": "2.7", "name": "Send Voyage Orders", "type": "sub", "highlighted": False},
            {"id": "2.8", "name": "Agency Nomination", "type": "sub", "highlighted": False},
            {"id": "2.9", "name": "Documentation Instructions", "type": "sub", "highlighted": True},
            {"id": "2.10", "name": "Inspection Nomination", "type": "sub", "highlighted": False},
            {"id": "2.11", "name": "Ship Updates - ETA, ETB, ETC", "type": "sub", "highlighted": True},
            {"id": "2.12", "name": "Bunkering Requirements", "type": "sub", "highlighted": False},
        ]
    },
    {
        "id": "3",
        "name": "Loading",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "3.1", "name": "Coordination with Agent on Berth Schedule", "type": "sub", "highlighted": False},
            {"id": "3.2", "name": "Possible Port Requirements", "type": "sub", "highlighted": False},
            {"id": "3.3", "name": "Coordination with Trader on Berth Schedule", "type": "sub", "highlighted": False},
            {"id": "3.4", "name": "Marine LOI Requirements", "type": "sub", "highlighted": True},
        ]
    },
    {
        "id": "4",
        "name": "Departure Loadport",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "4.1", "name": "Ensure Documents Onboard", "type": "sub", "highlighted": False},
            {"id": "4.2", "name": "Advise Next Destination", "type": "sub", "highlighted": False},
            {"id": "4.3", "name": "Check Cargo Quantity Loaded", "type": "sub", "highlighted": False},
            {"id": "4.4", "name": "Update DEX for BL Quantity", "type": "sub", "highlighted": True},
            {"id": "4.5", "name": "Review Cargo Quality", "type": "sub", "highlighted": True},
            {"id": "4.6", "name": "EDP", "type": "sub", "highlighted": True},
        ]
    },
    {
        "id": "5",
        "name": "Arrival at Disport",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "5.1", "name": "ETA Update", "type": "sub", "highlighted": False},
            {"id": "5.2", "name": "Marine LOI Requirements", "type": "sub", "highlighted": False},
            {"id": "5.3", "name": "Coordination with Agents and Ship", "type": "sub", "highlighted": False},
            {"id": "5.4", "name": "Documents Received?", "type": "sub", "highlighted": True},
        ]
    },
    {
        "id": "6",
        "name": "Discharge",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "6.1", "name": "Coordination with Agent on Berth Schedule", "type": "sub", "highlighted": False},
            {"id": "6.2", "name": "Confirmation of Receiver to Discharge", "type": "sub", "highlighted": False},
        ]
    },
    {
        "id": "7",
        "name": "Voyage Completion",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "7.1", "name": "Check Cargo Discharged", "type": "sub", "highlighted": False},
            {"id": "7.2", "name": "DEX Update", "type": "sub", "highlighted": True},
            {"id": "7.3", "name": "RADAR Update", "type": "sub", "highlighted": True},
        ]
    },
    {
        "id": "8",
        "name": "Post Voyage (Claims & Loss Reporting)",
        "type": "main",
        "highlighted": True,
        "completed": False,
        "sub_steps": [
            {"id": "8.1", "name": "Claims & Loss Reporting", "type": "sub", "highlighted": False},
            {"id": "8.2", "name": "Payment of Freight & Oil Charges", "type": "sub", "highlighted": False},
            {"id": "8.3", "name": "Invoicing for Freight and Oil Claims", "type": "sub", "highlighted": False},
            {"id": "8.4", "name": "Payment of Inspection", "type": "sub", "highlighted": False},
            {"id": "8.5", "name": "Import/Export Permit", "type": "sub", "highlighted": False},
        ]
    },
]