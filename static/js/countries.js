var countries = [
    { value: "Afghanistan" }
    { value: "Dominica" }
    { value: "Lesotho" }
    { value: "Sao Tome and Principe" }
    { value: "Albania" }
    { value: "Dominican Republic" }
    { value: "Liberia" }
    { value: "Saudi Arabia" }
    { value: "Algeria" }
    { value: "Ecuador" }
    { value: "Libya" }
    { value: "Senegal" }
    { value: "American Samoa" }
    { value: "Egypt, Arab Rep." }
    { value: "Liechtenstein" }
    { value: "Serbia" }
    { value: "Andean Region" }
    { value: "El Salvador" }
    { value: "Lithuania" }
    { value: "Seychelles" }
    { value: "Andorra" }
    { value: "Equatorial Guinea" }
    { value: "Luxembourg" }
    { value: "Sierra Leone" }
    { value: "Angola" }
    { value: "Eritrea" }
    { value: "Macao SAR, China" }
    { value: "Singapore" }
    { value: "Antigua and Barbuda" }
    { value: "Estonia" }
    { value: "Macedonia, FYR" }
    { value: "Sint Maarten (Dutch part)" }
    { value: "Argentina" }
    { value: "Ethiopia" }
    { value: "Madagascar" }
    { value: "Slovak Republic" }
    { value: "Armenia" }
    { value: "Faeroe Islands" }
    { value: "Malawi" }
    { value: "Slovenia" }
    { value: "Aruba" }
    { value: "Fiji" }
    { value: "Malaysia" }
    { value: "Solomon Islands" }
    { value: "Australia" }
    { value: "Finland" }
    { value: "Maldives" }
    { value: "Somalia" }
    { value: "Austria" }
    { value: "France" }
    { value: "Mali" }
    { value: "South Africa" }
    { value: "Azerbaijan" }
    { value: "French Polynesia" }
    { value: "Malta" }
    { value: "South Sudan" }
    { value: "Bahamas" }
    { value: "Gabon" }
    { value: "Marshall Islands" }
    { value: "Spain" }
    { value: "Bahrain" }
    { value: "Gambia" }
    { value: "Mauritania" }
    { value: "Sri Lanka" }
    { value: "Bangladesh" }
    { value: "Georgia" }
    { value: "Mauritius" }
    { value: "St. Kitts and Nevis" }
    { value: "Barbados" }
    { value: "Germany" }
    { value: "Mexico" }
    { value: "St. Lucia" }
    { value: "Belarus" }
    { value: "Ghana" }
    { value: "Micronesia, Fed. Sts." }
    { value: "St. Martin (French part)" }
    { value: "Belgium" }
    { value: "Greece" }
    { value: "Moldova" }
    { value: "St. Vincent and the Grenadines" }
    { value: "Belize" }
    { value: "Greenland" }
    { value: "Monaco" }
    { value: "Sudan" }
    { value: "Benin" }
    { value: "Grenada" }
    { value: "Mongolia" }
    { value: "Suriname" }
    { value: "Bermuda" }
    { value: "Guam" }
    { value: "Montenegro" }
    { value: "Swaziland" }
    { value: "Bhutan" }
    { value: "Guatemala" }
    { value: "Morocco" }
    { value: "Sweden" }
    { value: "Bolivia" }
    { value: "Guinea" }
    { value: "Mozambique" }
    { value: "Switzerland" }
    { value: "Bosnia and Herzegovina" }
    { value: "Guinea-Bissau" }
    { value: "Myanmar" }
    { value: "Syrian Arab Republic" }
    { value: "Botswana" }
    { value: "Guyana" }
    { value: "Namibia" }
    { value: "Tajikistan" }
    { value: "Brazil" }
    { value: "Haiti" }
    { value: "Nepal" }
    { value: "Tanzania" }
    { value: "Brunei Darussalam" }
    { value: "Honduras" }
    { value: "Netherlands" }
    { value: "Thailand" }
    { value: "Bulgaria" }
    { value: "Hong Kong SAR, China" }
    { value: "New Caledonia" }
    { value: "Timor-Leste" }
    { value: "Burkina Faso" }
    { value: "Hungary" }
    { value: "New Zealand" }
    { value: "Togo" }
    { value: "Burundi" }
    { value: "Iceland" }
    { value: "Nicaragua" }
    { value: "Tonga" }
    { value: "Cabo Verde" }
    { value: "India" }
    { value: "Niger" }
    { value: "Trinidad and Tobago" }
    { value: "Cambodia" }
    { value: "Indonesia" }
    { value: "Nigeria" }
    { value: "Tunisia" }
    { value: "Cameroon" }
    { value: "Iran, Islamic Rep." }
    { value: "Northern Mariana Islands" }
    { value: "Turkey" }
    { value: "Canada" }
    { value: "Iraq" }
    { value: "Norway" }
    { value: "Turkmenistan" }
    { value: "Cayman Islands" }
    { value: "Ireland" }
    { value: "Oman" }
    { value: "Turks and Caicos Islands" }
    { value: "Central African Republic" }
    { value: "Isle of Man" }
    { value: "Pakistan" }
    { value: "Tuvalu" }
    { value: "Chad" }
    { value: "Israel" }
    { value: "Palau" }
    { value: "Uganda" }
    { value: "Chile" }
    { value: "Italy" }
    { value: "Panama" }
    { value: "Ukraine" }
    { value: "China" }
    { value: "Jamaica" }
    { value: "Papua New Guinea" }
    { value: "United Arab Emirates" }
    { value: "Colombia" }
    { value: "Japan" }
    { value: "Paraguay" }
    { value: "United Kingdom" }
    { value: "Comoros" }
    { value: "Jordan" }
    { value: "Peru" }
    { value: "United States" }
    { value: "Congo, Dem. Rep." }
    { value: "Kazakhstan" }
    { value: "Philippines" }
    { value: "Uruguay" }
    { value: "Congo, Rep." }
    { value: "Kenya" }
    { value: "Poland" }
    { value: "Uzbekistan" }
    { value: "Costa Rica" }
    { value: "Kiribati" }
    { value: "Portugal" }
    { value: "Vanuatu" }
    { value: "Cote divoire" }
    { value: "Korea, Dem. Rep." }
    { value: "Puerto Rico" }
    { value: "Venezuela, RB" }
    { value: "Croatia" }
    { value: "Korea, Rep." }
    { value: "Qatar" }
    { value: "Vietnam" }
    { value: "Cuba" }
    { value: "Kuwait" }
    { value: "Romania" }
    { value: "Virgin Islands (U.S.)" }
    { value: "Curacao" }
    { value: "Kyrgyz Republic" }
    { value: "Russian Federation" }
    { value: "West Bank and Gaza" }
    { value: "Cyprus" }
    { value: "Lao PDR" }
    { value: "Rwanda" }
    { value: "Yemen, Rep." }
    { value: "Czech Republic" }
    { value: "Latvia" }
    { value: "Samoa" }
    { value: "Zambia" }
    { value: "Denmark" }
    { value: "Lebanon" }
    { value: "San Marino" }
    { value: "Zimbabwe" }
    { value: "Djibouti" }
];
