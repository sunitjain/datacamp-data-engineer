# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              false_values = ['No'],
                              true_values = ['Yes'])

# View the data
print(survey_subset.head())