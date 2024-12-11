


class ListingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Listing
        include_fk = True

    user = fields.Nested('UserSchema', only=['id', 'username'])
    skill = fields.Nested('SkillSchema', only=['id', 'name'])

listing_schema = ListingSchema()
listings_schema = ListingSchema(many=True)