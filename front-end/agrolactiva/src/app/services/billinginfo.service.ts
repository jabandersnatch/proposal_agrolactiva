import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { BillingInfoModel } from '../models/billinginfoModel';

@Injectable()
export class BillingInfoService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getBillingInfos(): Observable<BillingInfoModel[]> {
    return this.http.get<Array<BillingInfoModel>>(this.apiUrl + '/billinginfo/');
  }

  getBillingInfobyId(idBillingInfo: number): Observable<BillingInfoModel> {
    return this.http.get<BillingInfoModel>(this.apiUrl + '/billinginfo/' + idBillingInfo);
  }

  addBillingInfo(BillingInfo:BillingInfoModel): Observable<BillingInfoModel> {
    return this.http.post<BillingInfoModel>(`${this.apiUrl}/billinginfo/`, BillingInfoModel)
  }
}

