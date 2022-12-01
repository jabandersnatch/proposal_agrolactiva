export class ClientModel {
  id_person: string;
  organization: string;
  register_date: Date;

  public constructor(
    id_person: string,
    organization: string,
    register_date: Date
  ) {
    this.id_person = id_person;
    this.organization = organization;
    this.register_date = register_date;
  }
}
