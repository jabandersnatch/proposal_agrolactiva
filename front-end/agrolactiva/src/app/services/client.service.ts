import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { ClientModel } from '../models/clientModel';

@Injectable()
export class ClientService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getClients(): Observable<ClientModel[]> {
    return this.http.get<Array<ClientModel>>(this.apiUrl + '/client/');
  }

  getClientbyId(idClient: number): Observable<ClientModel> {
    return this.http.get<ClientModel>(this.apiUrl + '/client/' + idClient);
  }

  addClient(Client:ClientModel): Observable<ClientModel> {
    return this.http.post<ClientModel>(`${this.apiUrl}/client/`, ClientModel)
  }
}

