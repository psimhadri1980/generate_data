from faker.providers import BaseProvider

localized = False

class Provider(BaseProvider):
    """Implement custom Country provider for Faker."""
    
    COUNTRIES: [str] = [
            'Afganistan', 'Afrika Selatan', 'Afrika Tengah', 'Albania', 'Aljazair',
            'Amerika Serikat', 'Andorra', 'Angola', 'Antigua dan Barbuda',
            'Arab Saudi', 'Argentina', 'Armenia', 'Australia', 'Austria',
            'Azerbaijan', 'Bahama', 'Bahrain', 'Bangladesh', 'Barbados', 'Belanda',
            'Belarus', 'Belgia', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
            'Bosnia dan Herzegovina', 'Botswana', 'Brasil', 'Britania Raya',
            'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Ceko', 'Chad',
            'Chili', 'Denmark', 'Djibouti', 'Dominika', 'Ekuador', 'El Salvador',
            'Eritrea', 'Estonia', 'Ethiopia', 'Federasi Mikronesia', 'Fiji',
            'Filipina', 'Finlandia', 'Gabon', 'Gambia', 'Georgia', 'Ghana',
            'Grenada', 'Guatemala', 'Guinea', 'Guinea Khatulistiwa',
            'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hongaria', 'India',
            'Indonesia', 'Irak', 'Iran', 'Islandia', 'Israel', 'Italia', 'Jamaika',
            'Jepang', 'Jerman', 'Kamboja', 'Kamerun', 'Kanada', 'Kazakhstan',
            'Kenya', 'Kepulauan Marshall', 'Kepulauan Solomon', 'Kirgizstan',
            'Kiribati', 'Kolombia', 'Komoro', 'Korea Selatan', 'Korea Utara',
            'Kosta Rika', 'Kroasia', 'Kuba', 'Kuwait', 'Laos', 'Latvia', 'Lebanon',
            'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lituania',
            'Luksemburg', 'Madagaskar', 'Maladewa', 'Malawi', 'Malaysia', 'Mali',
            'Malta', 'Maroko', 'Mauritania', 'Mauritius', 'Meksiko', 'Mesir',
            'Moldova', 'Monako', 'Mongolia', 'Montenegro', 'Mozambik', 'Myanmar',
            'Namibia', 'Nauru', 'Nepal', 'Niger', 'Nigeria', 'Nikaragua',
            'Norwegia', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Pantai Gading',
            'Papua Nugini', 'Paraguay', 'Perancis', 'Peru', 'Polandia', 'Portugal',
            'Qatar', 'Republik Demokratik Kongo', 'Republik Dominika',
            'Republik Irlandia', 'Republik Kongo', 'Republik Makedonia',
            'Republik Rakyat Tiongkok', 'Rumania', 'Rusia', 'Rwanda',
            'Saint Kitts dan Nevis', 'Saint Lucia', 'Saint Vincent dan Grenadine',
            'Samoa', 'San Marino', 'São Tomé dan Príncipe', 'Selandia Baru',
            'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapura',
            'Siprus', 'Slovenia', 'Slowakia', 'Somalia', 'Spanyol', 'Sri Lanka',
            'Sudan', 'Sudan Selatan', 'Suriah', 'Suriname', 'Swaziland', 'Swedia',
            'Swiss', 'Tajikistan', 'Tanjung Verde', 'Tanzania', 'Thailand',
            'Timor Leste', 'Togo', 'Tonga', 'Trinidad dan Tobago', 'Tunisia',
            'Turki', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraina',
            'Uni Emirat Arab', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatikan',
            'Venezuela', 'Vietnam', 'Yaman', 'Yordania', 'Yunani', 'Zambia',
            'Zimbabwe',
        ]

    def country(self) -> int:
        return self.random_element(self.COUNTRIES)