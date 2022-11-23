import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { EmployeeModel } from '../models/employeeModel';

@Injectable()
export class EmployeeService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getEmployees(): Observable<EmployeeModel[]> {
    return this.http.get<Array<EmployeeModel>>(this.apiUrl + '/employee/');
  }

  getEmployeebyId(idEmployee: number): Observable<EmployeeModel> {
    return this.http.get<EmployeeModel>(this.apiUrl + '/employee/' + idEmployee);
  }

  addEmployee(Employee:EmployeeModel): Observable<EmployeeModel> {
    return this.http.post<EmployeeModel>(`${this.apiUrl}/employee/`, EmployeeModel)
  }
}

