export class ProviderModel {
  id_person: string;
  id_route: string;
  register_date: Date;

  public constructor(
    id_person: string,
    id_route: string,
    register_date: Date
  ) {
    this.id_person = id_person;
    this.id_route = id_route;
    this.register_date = register_date;
  }
}
