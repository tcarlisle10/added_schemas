from app.models import Skill

class SkillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Skill
        include_fk = True

skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)