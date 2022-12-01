import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';
import { PersonModel } from '../models/personModel';
import { map } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    return this.http.post<any>(this.apiUrl + 'auth/login/',
      { username, password }, httpOptions).pipe(
        map(user => {
        if( user && user.token) {
          localStorage.setItem("currentUser", JSON.stringify(user))
        }
        return user;
      }))
  }

  logout(){
    localStorage.removeItem('currentUser')
  }

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

