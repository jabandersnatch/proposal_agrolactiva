export class LocationModel {
  name: string;
  code: string;
  id_municipality: string;

  public constructor(
    name: string,
    code: string,
    id_municipality: string
  ) {
     this.name = name;
     this.code = code;
     this.id_municipality = id_municipality;
  }
}
