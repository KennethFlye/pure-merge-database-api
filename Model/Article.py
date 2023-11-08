import datetime


class Article:

    def __init__(self, id, submitter, submitter_is_preferred, authors, authors_is_preferred, title, title_is_preferred, comments, comments_is_preferred, journalRef, journalRef_is_preferred, doi, doi_is_preferred, reportNumber, reportNumber_is_preferred, categories, categories_is_preferred, license, license_is_preferred, abstract, abstract_is_preferred, versions, versions_is_preferred, updateDate, updateDate_is_preferred, group):
        self.id = id
        self.submitter = submitter
        self.submitter_is_preferred = submitter_is_preferred
        self.authors = authors
        self.authors_is_preferred = authors_is_preferred
        self.title = title
        self.title_is_preferred = title_is_preferred
        self.comments = comments
        self.comments_is_preferred = comments_is_preferred
        self.journalRef = journalRef
        self.journalRef_is_preferred = journalRef_is_preferred
        self.doi = doi
        self.doi_is_preferred = doi_is_preferred
        self.reportNumber = reportNumber
        self.reportNumber_is_preferred = reportNumber_is_preferred
        self.categories = categories
        self.categories_is_preferred = categories_is_preferred
        self.license = license
        self.license_is_preferred = license_is_preferred
        self.abstract = abstract
        self.abstract_is_preferred = abstract_is_preferred
        self.versions = versions
        self.versions_is_preferred = versions_is_preferred
        self.updateDate = updateDate
        self.updateDate_is_preferred = updateDate_is_preferred
        self.group = group

    def __str__(self):
        return f'Id: {self.id}, submitter: {self.submitter}, author: {self.author}, title: {self.title}, comments: {self.comments}, journalRef: {self.journalRef}, doi: {self.doi}, reportNumber: {self.reportNumber}, categories: {self.categories}, license: {self.license}, abstract: {self.abstract}, versions: {self.versions}, updateDate: {self.updateDate}'

    def getListOfVariables(self):
        variables = ['id', 'submitter', 'author', 'title', 'comments', 'journalRef', 'doi', 'reportNumber', 'categories', 'license', 'abstract', 'versions', 'updateDate']

        return variables

