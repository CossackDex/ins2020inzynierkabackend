
from .models import UserSurvey

def parse_user_preferences(user_survey: UserSurvey) -> dict:
    user_preferences = dict()
    user_preferences['programming_languages'] = list()
    user_preferences['topics'] = list()
    user_preferences['length'] = list()
    user_preferences['publisher'] = list()
    # programming languages
    if user_survey.java: user_preferences['programming_languages'].append('java')
    if user_survey.python: user_preferences['programming_languages'].append('python')
    if user_survey.js: user_preferences['programming_languages'].append('js')
    if user_survey.csharp: user_preferences['programming_languages'].append('csharp')
    if user_survey.cpp: user_preferences['programming_languages'].append('cpp')
    if user_survey.go: user_preferences['programming_languages'].append('go')
    if user_survey.r: user_preferences['programming_languages'].append('r')
    if user_survey.swift: user_preferences['programming_languages'].append('swift')
    if user_survey.php: user_preferences['programming_languages'].append('php')
    if user_survey.sql: user_preferences['programming_languages'].append('sql')
    # book topics
    if user_survey.webdev: user_preferences['topics'].append('webdev')
    if user_survey.machinelearning: user_preferences['topics'].append('machinelearning')
    if user_survey.database: user_preferences['topics'].append('database')
    if user_survey.algorithms: user_preferences['topics'].append('algorithms')
    if user_survey.softwaredev: user_preferences['topics'].append('softwaredev')
    # prefered book length
    if user_survey.long: user_preferences['length'].append('long')
    if user_survey.medium: user_preferences['length'].append('medium')
    if user_survey.short: user_preferences['length'].append('short')
    if user_survey.length_dontcare: user_preferences['length'].append('length_dontcare')
    # publisher
    if user_survey.the_pragmatic_bookshelf: user_preferences['publisher'].append('the_pragmatic_bookshelf')
    if user_survey.manning_publications: user_preferences['publisher'].append('manning_publications')
    if user_survey.oreilly_media: user_preferences['publisher'].append('oreilly_media')
    if user_survey.no_starch_press: user_preferences['publisher'].append('no_starch_press')
    if user_survey.packt_publishing: user_preferences['publisher'].append('packt_publishing')
    if user_survey.que: user_preferences['publisher'].append('que')
    if user_survey.leanpub: user_preferences['publisher'].append('leanpub')
    if user_survey.peachpit: user_preferences['publisher'].append('peachpit')
    if user_survey.publisher_dontcare: user_preferences['publisher'].append('publisher_dontcare')
    return user_preferences
