import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { PersonModel } from '../models/personModel';

@Injectable()
export class PersonService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getPersons(): Observable<PersonModel[]> {
    return this.http.get<Array<PersonModel>>(this.apiUrl + '/person/');
  }

  getPersonbyId(idPerson: number): Observable<PersonModel> {
    return this.http.get<PersonModel>(this.apiUrl + '/person/' + idPerson);
  }

  addPerson(Person:PersonModel): Observable<PersonModel> {
    return this.http.post<PersonModel>(`${this.apiUrl}/person/`, PersonModel)
  }
}

