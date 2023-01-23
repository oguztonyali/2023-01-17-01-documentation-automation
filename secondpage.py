from tkinter import *
import tkinter.ttk as ttk

# ---------------------------- Colours ------------------------------------------- #
DARK = "#222831"
GRAY = "#393E46"
BLUE = "#00ADB5"
WHITE = "#EEEEEE"
FONT_NAME = "Courier"
country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
# -------------------------------------------------------------------------------- #


def second_page():
    """Second page contains choosing options on tender and constant documents. Also, tender information such
    as quotation number, tender name etc. can be written on this page."""
    window_second = Tk()
    window_second.title("Tender Documentation Helper v.0.2")
    window_second.config(padx=30, pady=30, bg=DARK)

    canvas = Canvas(width=256, height=256, bg=DARK, highlightthickness=0)
    folder_img = PhotoImage(file="folders.png")
    canvas.create_image(128, 128, image=folder_img)
    canvas.grid(row=0, column=0, columnspan=8)

    tender_no_label = Label(text="Tender No:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    tender_no_label.grid(row=1, column=1)

    tender_no_entry = Entry(width=30)
    tender_no_entry.grid(row=1, column=2)

    tender_name_label = Label(text="Tender Name:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    tender_name_label.grid(row=1, column=4, sticky="W")

    tender_name_entry = Entry(width=30)
    tender_name_entry.grid(row=1, column=5)

    country_choose = Label(text="Country:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    country_choose.grid(row=2, column=1, sticky="W")

    country_box = ttk.Combobox(window_second, width=27)
    country_box.grid(row=2, column=2)
    country_box["values"] = country_list

    select_tender_folder_label = Label(text="Select where to create Rar File:", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    select_tender_folder_label.grid(row=3, column=0, sticky="W", columnspan=3, pady=10)

    select_tender_folder_entry = Entry(width=90)
    select_tender_folder_entry.grid(row=3, column=3, columnspan=5, sticky="W")

    constant_label = Label(text="Constant Files", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    constant_label.grid(row=4, column=1, columnspan=3)

    tender_files_label = Label(text="Tender Files", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    tender_files_label.grid(row=4, column=4, columnspan=4)

    catalogue_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    catalogue_checkbox.grid(row=5, column=0)

    catalogue_label = Label(text="Catalogue", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    catalogue_label.grid(row=5, column=1)

    iso_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    iso_checkbox.grid(row=6, column=0)

    iso_label = Label(text="ISO Certificates", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    iso_label.grid(row=6, column=1)

    iec_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    iec_checkbox.grid(row=7, column=0)

    iec_label = Label(text="IEC Certificates", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    iec_label.grid(row=7, column=1)

    test_reports_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    test_reports_checkbox.grid(row=8, column=0)

    test_reports_label = Label(text="Test Reports", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    test_reports_label.grid(row=8, column=1)

    references_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    references_checkbox.grid(row=9, column=0)

    references_label = Label(text="References", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    references_label.grid(row=9, column=1)

    company_profile_checkbox = Checkbutton(bg=DARK, activebackground=DARK, highlightthickness=0)
    company_profile_checkbox.grid(row=10, column=0)

    company_profile_label = Label(text="Company Profile", fg=BLUE, bg=DARK, font=(FONT_NAME, 12, "bold"))
    company_profile_label.grid(row=10, column=1)

# -------------------------------------------------------------------------------- #

    save_button = Button(text="Save", width=15)
    save_button.grid(row=15, column=1)

    clear_tender_button = Button(text="Clear Tender", width=15)
    clear_tender_button.grid(row=15, column=2)

    clear_all_button = Button(text="Clear All", width=15)
    clear_all_button.grid(row=15, column=3)

    next_button = Button(text="Previous", width=15)
    next_button.grid(row=15, column=4)

    next_button = Button(text="Next", width=15)
    next_button.grid(row=15, column=5)

    help_button = Button(text="?", width=5, bg=DARK, font=(FONT_NAME, 12, "bold"))
    help_button.grid(row=15, column=6)


    window_second.mainloop()
