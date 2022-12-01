import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { ContactInfoModel } from '../models/contactinfoModel';

@Injectable()
export class ContactInfoService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getContactInfos(idPerson: number): Observable<ContactInfoModel[]> {
    return this.http.get<Array<ContactInfoModel>>(this.apiUrl + '/contactinfo/' + idPerson);
  }

  getContactInfobyId(idContactInfo: number): Observable<ContactInfoModel> {
    return this.http.get<ContactInfoModel>(this.apiUrl + '/contactinfo/' + idContactInfo);
  }

  addContactInfo(ContactInfo:ContactInfoModel): Observable<ContactInfoModel> {
    return this.http.post<ContactInfoModel>(`${this.apiUrl}/contactinfo/`, ContactInfoModel)
  }
}

