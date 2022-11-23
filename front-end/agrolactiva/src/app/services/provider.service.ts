import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { ProviderModel } from '../models/providerModel';

@Injectable()
export class ProviderService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getProviders(): Observable<ProviderModel[]> {
    return this.http.get<Array<ProviderModel>>(this.apiUrl + '/provider/');
  }

  getProviderbyId(idProvider: number): Observable<ProviderModel> {
    return this.http.get<ProviderModel>(this.apiUrl + '/provider/' + idProvider);
  }

  addProvider(Provider:ProviderModel): Observable<ProviderModel> {
    return this.http.post<ProviderModel>(`${this.apiUrl}/provider/`, ProviderModel)
  }
}

