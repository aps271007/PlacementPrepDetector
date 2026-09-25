from pydantic import BaseModel, Field
from typing import Optional, List

#contact details
class Contact(BaseModel):
    full_name : Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    github_url : Optional[str] = None
    linkedin_url : Optional[str] = None
    portfolio_url : Optional[str] = None
    coding_profiles: List[str] = Field(default_factory=list)

#education details
class Education(BaseModel):
    institution: str
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_year: Optional[str] = None
    end_year: Optional[str] = None
    gpa_or_percentage: Optional[str] = None

#skills
class Skills(BaseModel):
    languages: List[str] = Field(default_factory=list)
    frameworks: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    tools_and_platforms : List[str] = Field(default_factory=list)

#project details

class Project(BaseModel):
    title:str
    description: Optional[str] = None
    tech_stack: List[str] = Field(default_factory=list)
    repo_url: Optional[str] = None
    live_url: Optional[str] = None

class Experience(BaseModel):
    company: str
    role: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None

class Certification(BaseModel):
    name: str
    issuer: Optional[str] = None
    issue_date: Optional[str] = None
    credential_url: Optional[str] = None

class ResumeData(BaseModel):
    contact: Contact
    education: List[Education] = Field(default_factory = list)
    skills : Skills
    projects : List[Project] = Field(default_factory = list)
    experience  : List[Experience] = Field(default_factory = list)
    certifications : List[Certification] = Field(default_factory = list)