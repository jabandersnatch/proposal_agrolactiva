import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { MunicipalityModel } from '../models/municipalityModel';

@Injectable()
export class MunicipalityService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getMunicipalities(): Observable<MunicipalityModel[]> {
    return this.http.get<Array<MunicipalityModel>>(this.apiUrl + '/municipality/');
  }

  getMunicipalitybyId(idMunicipality: number): Observable<MunicipalityModel> {
    return this.http.get<MunicipalityModel>(this.apiUrl + '/municipality/' + idMunicipality);
  }

  addMunicipality(Municipality:MunicipalityModel): Observable<MunicipalityModel> {
    return this.http.post<MunicipalityModel>(`${this.apiUrl}/municipality/`, MunicipalityModel)
  }
}

