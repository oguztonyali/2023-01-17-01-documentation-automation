from tkinter import *
import tkinter.ttk as ttk
import functions_for_all

# Tender Documentation Automation Project

# ---------------------------- Colours ------------------------------------------- #
DARK = "#222831"
GRAY = "#393E46"
BLUE = "#00ADB5"
WHITE = "#EEEEEE"
FONT_NAME = "Courier"
country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
                'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
                'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
                'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba',
                'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
                'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
                'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China',
                'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
                'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia',
                'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
                'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
                'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
                'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
                'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
                'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands',
                'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia',
                'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
                'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of",
                'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon',
                'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
                'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
                'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro',
                'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
                'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island',
                'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied',
                'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal',
                'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy',
                'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia',
                'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa',
                'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
                'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands',
                'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka',
                'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland',
                'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of',
                'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
                'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan',
                'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British',
                'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']


# -------------------------------------------------------------------------------- #

def first_page():
    window_first = Tk()
    window_first.title("Tender Documentation Helper v.0.2")
    window_first.config(padx=30, pady=20, bg=DARK)

    canvas = Canvas(width=256, height=256, bg=DARK, highlightthickness=0)
    folder_img = PhotoImage(file="folders.png")
    canvas.create_image(128, 128, image=folder_img)
    canvas.grid(row=0, column=0, columnspan=6)

    tender_browsing_label = Label(text="Please Confirm Documents Locations", fg=BLUE, bg=DARK, font=(
        FONT_NAME, 14, "bold"))
    tender_browsing_label.grid(row=1, column=0, columnspan=6, pady=5)

    catalogue_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    catalogue_checkbox.grid(row=2, column=0)

    catalogue_address_label = Label(text="Catalogue:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    catalogue_address_label.grid(row=2, column=1)

    catalogue_address_entry = Entry(width=30)
    catalogue_address_entry.grid(row=2, column=2, padx=2)

    catalogue_address_button = Button(text="Browse")
    catalogue_address_button.grid(row=2, column=3, padx=2, pady=10)

    iso_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    iso_checkbox.grid(row=3, column=0)

    iso_address_label = Label(text="ISO Certificates:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    iso_address_label.grid(row=3, column=1)

    iso_address_entry = Entry(width=30)
    iso_address_entry.grid(row=3, column=2, padx=2)

    iso_address_button = Button(text="Browse")
    iso_address_button.grid(row=3, column=3, padx=2, pady=10)

    iec_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    iec_checkbox.grid(row=4, column=0)

    iec_address_label = Label(text="IEC Certificates:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    iec_address_label.grid(row=4, column=1)

    iec_address_entry = Entry(width=30)
    iec_address_entry.grid(row=4, column=2, padx=2)

    iec_address_button = Button(text="Browse")
    iec_address_button.grid(row=4, column=3, padx=2, pady=10)

    references_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    references_checkbox.grid(row=5, column=0)

    references_address_label = Label(text="References:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    references_address_label.grid(row=5, column=1)

    references_address_entry = Entry(width=30)
    references_address_entry.grid(row=5, column=2, padx=2)

    references_address_button = Button(text="Browse")
    references_address_button.grid(row=5, column=3, padx=2, pady=10)

    company_profile_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    company_profile_checkbox.grid(row=6, column=0)

    company_profile_address_label = Label(text="Company Profile", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    company_profile_address_label.grid(row=6, column=1)

    company_profile_address_entry = Entry(width=30)
    company_profile_address_entry.grid(row=6, column=2, padx=2)

    company_profile_address_button = Button(text="Browse")
    company_profile_address_button.grid(row=6, column=3, padx=2, pady=10)

    financial_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    financial_address_checkbox.grid(row=7, column=0)

    financial_address_label = Label(text="Financial Reports:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    financial_address_label.grid(row=7, column=1)

    financial_address_entry = Entry(width=30)
    financial_address_entry.grid(row=7, column=2, padx=2)

    financial_address_button = Button(text="Browse")
    financial_address_button.grid(row=7, column=3, padx=2, pady=10)

    audit_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    audit_address_checkbox.grid(row=2, column=4)

    audit_address_label = Label(text="Audit Reports:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    audit_address_label.grid(row=2, column=5)

    audit_address_entry = Entry(width=30)
    audit_address_entry.grid(row=2, column=6, padx=2)

    audit_address_button = Button(text="Browse")
    audit_address_button.grid(row=2, column=7, padx=2, pady=10)

    shareholders_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    shareholders_address_checkbox.grid(row=3, column=4)

    shareholders_address_label = Label(text="Shareholders:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    shareholders_address_label.grid(row=3, column=5)

    shareholders_address_entry = Entry(width=30)
    shareholders_address_entry.grid(row=3, column=6, padx=2)

    shareholders_address_button = Button(text="Browse")
    shareholders_address_button.grid(row=3, column=7, padx=2, pady=10)

    qhse_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    qhse_address_checkbox.grid(row=4, column=4)

    qhse_address_label = Label(text="QHSE Documents:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    qhse_address_label.grid(row=4, column=5)

    qhse_address_entry = Entry(width=30)
    qhse_address_entry.grid(row=4, column=6, padx=2)

    qhse_address_button = Button(text="Browse")
    qhse_address_button.grid(row=4, column=7, padx=2, pady=10)

    hse_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    hse_address_checkbox.grid(row=5, column=4)

    hse_stats_address_label = Label(text="HSE Statistics:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    hse_stats_address_label.grid(row=5, column=5)

    hse_stats_address_entry = Entry(width=30)
    hse_stats_address_entry.grid(row=5, column=6, padx=2)

    hse_stats_address_button = Button(text="Browse")
    hse_stats_address_button.grid(row=5, column=7, padx=2, pady=10)

    company_stats_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    company_stats_address_checkbox.grid(row=6, column=4)

    company_stats_address_label = Label(text="Company Statistics:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    company_stats_address_label.grid(row=6, column=5)

    company_stats_address_entry = Entry(width=30)
    company_stats_address_entry.grid(row=6, column=6, padx=2)

    company_stats_address_button = Button(text="Browse")
    company_stats_address_button.grid(row=6, column=7, padx=2, pady=10)

    test_reports_address_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    test_reports_address_checkbox.grid(row=7, column=4)

    test_reports_address_label = Label(text="Test Reports:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    test_reports_address_label.grid(row=7, column=5)

    test_reports_address_entry = Entry(width=30)
    test_reports_address_entry.grid(row=7, column=6, padx=2)

    test_reports_address_button = Button(text="Browse")
    test_reports_address_button.grid(row=7, column=7, padx=2, pady=10)


    save_button = Button(text="Save", width=20)
    save_button.grid(row=13, column=0, padx=2, pady=5)

    clear_all_button = Button(text="Clear All", width=20)
    clear_all_button.grid(row=13, column=2, padx=2)

    next_button = Button(text="Next", width=20, command=functions_for_all.first_to_next)
    next_button.grid(row=13, column=4, padx=2)

    help_button = Button(text="?", width=5, bg=DARK, font=(FONT_NAME, 12, "bold"))
    help_button.grid(row=13, column=6, padx=10)

    window_first.mainloop()
