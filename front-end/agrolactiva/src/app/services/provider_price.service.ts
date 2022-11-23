import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { ProviderPriceModel } from '../models/provider_priceModel';

@Injectable()
export class ProviderPriceService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getProviderPrices(): Observable<ProviderPriceModel[]> {
    return this.http.get<Array<ProviderPriceModel>>(this.apiUrl + '/provider_price/');
  }

  getProviderPricebyId(idProviderPrice: number): Observable<ProviderPriceModel> {
    return this.http.get<ProviderPriceModel>(this.apiUrl + '/provider_price/' + idProviderPrice);
  }

  addProviderPrice(ProviderPrice:ProviderPriceModel): Observable<ProviderPriceModel> {
    return this.http.post<ProviderPriceModel>(`${this.apiUrl}/provider_price/`, ProviderPriceModel)
  }
}

