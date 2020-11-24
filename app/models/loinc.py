from sqlalchemy import Column
from sqlalchemy import String, Integer, DateTime
from db.connection import db
from models.lab_lonic_mapping import LabLonicMapping

class Loinc(db.Model):

    __table_args__ = {'schema': 'config'}
    __table_name__ = 'loinc'

    loinc_num = Column(String, primary_key=True, autoincrement=True)
    component = Column(String)
    property = Column(String)
    time_aspct = Column(String)
    scale_typ = Column(String)
    method_typ = Column(String)
    versionlastchanged = Column(String)
    chng_type = Column(String)
    definitiondescription = Column(String)
    status = Column(String)
    consumer_name = Column(String)
    classtype = Column(Integer)
    formula = Column(String)
    species = Column(String)
    exmpl_answers = Column(String)
    survey_quest_text = Column(String)
    survey_quest_src = Column(String)
    unitsrequired = Column(String)
    submitted_units = Column(String)
    relatednames2 = Column(String)
    shortname = Column(String)
    order_obs = Column(String)
    cdisc_common_tests = Column(String)
    hl7_field_subfield_id = Column(String)
    external_copyright_notice = Column(String)
    example_units = Column(String)
    long_common_name = Column(String)
    unitsandrange = Column(String)
    example_ucum_units = Column(String)
    example_si_ucum_units = Column(String)
    status_reason = Column(String)
    status_text = Column(String)
    change_reason_public = Column(String)
    common_test_rank = Column(Integer)
    common_order_rank = Column(Integer)
    common_si_test_rank = Column(Integer)
    hl7_attachment_structure = Column(String)
    externalcopyrightlink = Column(String)
    paneltype = Column(String)
    askatorderentry = Column(String)
    associatedobservations = Column(String)
    versionfirstreleased = Column(String)
    validhl7attachmentrequest = Column(String)
    displayname = Column(String)
    system = Column(String)
    classes = Column('class',String)
    external_copyright_link = Column(String)


    def find_all(self, page_no=1, limit=10, filters=None):
        lst = list()
        total = int()
        print('*******', filters)
        if isinstance(filters, int):
            total = db.session.query(
                                Loinc.loinc_num,
                                LabLonicMapping.lab_id
                                ).filter(
                                    Loinc.loinc_num == LabLonicMapping.loinc_num,
                                    LabLonicMapping.lab_id == filters
                                ).count()

            result = db.session.query(
                                Loinc.loinc_num,
                                Loinc.component,
                                Loinc.property,
                                Loinc.status,
                                Loinc.shortname,
                                Loinc.method_typ,
                                Loinc.scale_typ,
                                LabLonicMapping.lab_id
                                ).filter(
                                    Loinc.loinc_num == LabLonicMapping.loinc_num,
                                    LabLonicMapping.lab_id == filters
                                ).paginate(
                                         page=int(page_no), 
                                         error_out=False, 
                                         max_per_page=int(limit)
                                )
            for row in [row._asdict() for row in result.items]:
                row.pop('_sa_instance_state', None)
                lst.append(row)

        elif filters == None:
            total = db.session.query(Loinc).count()
            result = db.session.query(
                                Loinc.loinc_num,
                                Loinc.component,
                                Loinc.property,
                                Loinc.status,
                                Loinc.shortname,
                                Loinc.method_typ,
                                Loinc.scale_typ
                                ).paginate(
                                         page=int(page_no), 
                                         error_out=False, 
                                         max_per_page=int(limit)
                                )
            for row in [row._asdict() for row in result.items]:
                row.pop('_sa_instance_state', None)
                lst.append(row)
        
        elif isinstance(filters, dict):
            total = db.session.query(
                                Loinc.loinc_num
                                ).filter(
                                    Loinc.component.ilike('%'+  filters.get('component')  +'%')
                                ).count()

            result = db.session.query(
                                Loinc.loinc_num,
                                Loinc.component,
                                Loinc.property,
                                Loinc.status,
                                Loinc.shortname,
                                Loinc.method_typ,
                                Loinc.scale_typ
                                ).filter(
                                    Loinc.component.ilike('%'+  filters.get('component')  +'%')
                                ).paginate(
                                         page=int(page_no), 
                                         error_out=False, 
                                         max_per_page=int(limit)
                                )
            for row in [row._asdict() for row in result.items]:
                row.pop('_sa_instance_state', None)
                lst.append(row)

        else:
            total = db.session.query(
                                Loinc.loinc_num,
                                LabLonicMapping.lab_id
                                ).filter(
                                    Loinc.loinc_num == LabLonicMapping.loinc_num
                                ).filter_by(
                                    **filters
                                ).count()

            result = db.session.query(
                                Loinc.loinc_num,
                                Loinc.component,
                                Loinc.property,
                                Loinc.status,
                                Loinc.shortname,
                                Loinc.method_typ,
                                Loinc.scale_typ,
                                LabLonicMapping.lab_id
                                ).filter(
                                    Loinc.loinc_num == LabLonicMapping.loinc_num
                                ).filter_by(
                                    **filters
                                ).paginate(
                                         page=int(page_no), 
                                         error_out=False, 
                                         max_per_page=int(limit)
                                )
            for row in [row._asdict() for row in result.items]:
                row.pop('_sa_instance_state', None)
                lst.append(row)

        return lst, total