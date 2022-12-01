export class PersonModel {
  first_name: string;
  last_name: string;
  document_type: string;
  document_number: string;

  public constructor(
    first_name: string,
    last_name: string,
    document_type: string,
    document_number: string
  ) {
     this.first_name = first_name;
     this.last_name = last_name;
     this.document_type = document_type;
     this.document_number = document_number;
  }
}
