export class ContactInfoModel {
  id_person: string;
  phone_number: string;
  email: string;

  public constructor(
    id_person: string,
    phone_number: string,
    email: string
  ) {
    this.id_person = id_person;
    this.phone_number = phone_number;
    this.email = email;
  }
}
