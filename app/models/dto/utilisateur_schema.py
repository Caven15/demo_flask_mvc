from marshmallow import Schema, fields, validate

class UtilisateurSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    statut_compte = fields.Boolean(dump_only=True)

class UtilisateurRegisterSchema(UtilisateurSchema):
    password = fields.String(required=True, validate=validate.Length(min=8))