from sqlalchemy import Column
from sqlalchemy import String, Integer
from db.connection import db


class LabDetails(db.Model):

    __table_args__ = {'schema': 'config'}
    __table_name__ = 'lab_details'

    lab_id = Column(Integer, primary_key=True, autoincrement=True)
    clia = Column(String, nullable=False)
    laboratory_type = Column(String, nullable=False)
    certificate_type = Column(String, nullable=False)
    laboratory_name_address = Column(String, nullable=False)
    laboratory_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    web_site_address = Column(String, nullable=False)

    def find_all(self, page_no=1, limit=10):
        lst = list()
        result = LabDetails.query.paginate(page=int(page_no), error_out=False, max_per_page=int(limit))
        for row in [row.__dict__ for row in result.items]:
            row.pop('_sa_instance_state', None)
            lst.append(row)
        return lst, LabDetails.query.count()



