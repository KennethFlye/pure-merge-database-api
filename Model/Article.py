import datetime


class Article:

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def submitter(self):
        return self._submitter

    @submitter.setter
    def submitter(self, value):
        self._submitter = value

    @property
    def submitter_is_preferred(self):
        return self._submitter_is_preferred

    @submitter_is_preferred.setter
    def submitter_is_preferred(self, value):
        self._submitter_is_preferred = value

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        self._authors = value

    @property
    def authors_is_preferred(self):
        return self._authors_is_preferred

    @authors_is_preferred.setter
    def authors_is_preferred(self, value):
        self._authors_is_preferred = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def title_is_preferred(self):
        return self._title_is_preferred

    @title_is_preferred.setter
    def title_is_preferred(self, value):
        self._title_is_preferred = value

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value

    @property
    def comments_is_preferred(self):
        return self._comments_is_preferred

    @comments_is_preferred.setter
    def comments_is_preferred(self, value):
        self._comments_is_preferred = value
        
    @property
    def journal_ref(self):
        return self._journal_ref
    
    @journal_ref.setter
    def journal_ref(self, value):
        self._journal_ref = value
    
    @property
    def journal_ref_is_preferred(self):
        return self._journal_ref_is_preferred
    
    @journal_ref_is_preferred.setter
    def journal_ref_is_preferred(self, value):
        self._journal_ref_is_preferred = value

    @property
    def doi(self):
        return self._doi

    @doi.setter
    def doi(self, value):
        self._doi = value

    @property
    def doi_is_preferred(self):
        return self._doi_is_preferred

    @doi_is_preferred.setter
    def doi_is_preferred(self, value):
        self._doi_is_preferred = value
        
    @property
    def report_number(self):
        return self._report_number
    
    @report_number.setter
    def report_number(self, value):
        self._report_number = value

    @property
    def report_number_is_preferred(self):
        return self._report_number_is_preferred

    @report_number_is_preferred.setter
    def report_number_is_preferred(self, value):
        self._report_number_is_preferred = value

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = value

    @property
    def categories_is_preferred(self):
        return self._categories_is_preferred

    @categories_is_preferred.setter
    def categories_is_preferred(self, value):
        self._categories_is_preferred = value

    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, value):
        self._license = value

    @property
    def license_is_preferred(self):
        return self._license_is_preferred

    @license_is_preferred.setter
    def license_is_preferred(self, value):
        self._license_is_preferred = value

    @property
    def abstract(self):
        return self._abstract

    @abstract.setter
    def abstract(self, value):
        self._abstract = value

    @property
    def abstract_is_preferred(self):
        return self._abstract_is_preferred

    @abstract_is_preferred.setter
    def abstract_is_preferred(self, value):
        self._abstract_is_preferred = value

    @property
    def versions(self):
        return self._versions

    @versions.setter
    def versions(self, value):
        self._versions = value

    @property
    def versions_is_preferred(self):
        return self._versions_is_preferred

    @versions_is_preferred.setter
    def versions_is_preferred(self, value):
        self._versions_is_preferred = value

    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value

    @property
    def update_date_is_preferred(self):
        return self._update_date_is_preferred

    @update_date_is_preferred.setter
    def update_date_is_preferred(self, value):
        self._update_date_is_preferred = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    def __init__(self):
        self.id = None
        self.submitter = None
        self.submitter_is_preferred = None
        self.authors = None
        self.authors_is_preferred = None
        self.title = None
        self.title_is_preferred = None
        self.comments = None
        self.comments_is_preferred = None
        self.journal_ref = None
        self.journal_ref_is_preferred = None
        self.doi = None
        self.doi_is_preferred = None
        self.reportNumber = None
        self.reportNumber_is_preferred = None
        self.categories = None
        self.categories_is_preferred = None
        self.license = None
        self.license_is_preferred = None
        self.abstract = None
        self.abstract_is_preferred = None
        self.versions = None
        self.versions_is_preferred = None
        self.updateDate = None
        self.updateDate_is_preferred = None
        self.group = None

    def to_json(self):
        return {
            "Id": self.id,
            "submitter": self.submitter,
            "submitter_is_preferred": self.submitter_is_preferred,
            "author": self.authors,
            "author_is_preferred": self.authors_is_preferred,
            "title": self.title,
            "title_is_preferred": self.title_is_preferred,
            "comments": self.comments,
            "comments_is_preferred": self.comments_is_preferred,
            "journalRef": self.journal_ref,
            "journalRef_is_preferred": self.journal_ref_is_preferred,
            "doi": self.doi,
            "doi_is_preferred": self.doi_is_preferred,
            "reportNumber": self.report_number,
            "reportNumber_is_preferred": self.report_number_is_preferred,
            "categories": self.categories,
            "categories_is_preferred": self.categories_is_preferred,
            "license": self.license,
            "license_is_preferred": self.license_is_preferred,
            "abstract": self.abstract,
            "abstract_is_preferred": self.abstract_is_preferred,
            "versions": self.versions,
            "versions_is_preferred": self.versions_is_preferred,
            "update_date": str(self.update_date),  # NOTE, DATE IS NOW A STRING, VERY BIG NOTE HERE PLS DON'T FORGET
            "update_date_is_preferred": self.update_date_is_preferred,
            "group": self.group
        }
