from pydantic import BaseModel, Field


class PersonalInfo(BaseModel):
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    links: list[str] = Field(default_factory=list)


class ProfessionalInfo(BaseModel):
    target_roles: list[str] = Field(default_factory=list)
    years_of_experience: float | None = None


class SkillsInfo(BaseModel):
    hard_skills: list[str] = Field(default_factory=list)
    soft_skills: list[str] = Field(default_factory=list)


class LanguageInfo(BaseModel):
    language: str = ""
    level: str = ""


class Experience(BaseModel):
    title: str = ""
    company: str = ""
    dates: str = ""
    description: str = ""
    technologies: list[str] = Field(default_factory=list)


class Education(BaseModel):
    degree: str = ""
    institution: str = ""
    dates: str = ""


class CandidateProfile(BaseModel):
    personal: PersonalInfo = Field(default_factory=PersonalInfo)
    professional: ProfessionalInfo = Field(default_factory=ProfessionalInfo)
    summary: str = ""
    skills: SkillsInfo = Field(default_factory=SkillsInfo)
    experiences: list[Experience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    languages: list[LanguageInfo] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)