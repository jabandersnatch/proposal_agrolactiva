import { LocationModel } from "./locationModel";

export class EmployeeModel {
  id_person: string;
  salary: number;
  start_date: Date;
  end_date: Date;

  public constructor(
    id_person: string,
    salary: number,
    start_date: Date,
    end_date: Date,
  ) {
    this.id_person = id_person;
    this.salary = salary;
    this.start_date = start_date;
    this.end_date = end_date;
  }
}
