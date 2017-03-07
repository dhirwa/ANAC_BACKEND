from marshmallow import Schema,fields

class ApplicationSchema(Schema):
    id = fields.Integer(dump_only=True)
    data = fields.String()
    regDate = fields.Date()

appl_schema = ApplicationSchema()
appls_schema = ApplicationSchema(many = True)


class Admin_userSchema(Schema):
    id=fields.Integer(dump_only=True)
    first_name=fields.String()
    last_name=fields.String()
    username=fields.String()
    email=fields.String()
    password=fields.String()
    regDate=fields.Date()

useradmin_schema=Admin_userSchema()
useradmins_schema=Admin_userSchema(many=True)
