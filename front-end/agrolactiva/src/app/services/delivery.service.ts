import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { DeliveryModel } from '../models/deliveryModel';

@Injectable()
export class DeliveryService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getDeliveries(): Observable<DeliveryModel[]> {
    return this.http.get<Array<DeliveryModel>>(this.apiUrl + '/delivery/');
  }

  getDeliverybyId(idDelivery: number): Observable<DeliveryModel> {
    return this.http.get<DeliveryModel>(this.apiUrl + '/delivery/' + idDelivery);
  }

  addDelivery(Delivery:DeliveryModel): Observable<DeliveryModel> {
    return this.http.post<DeliveryModel>(`${this.apiUrl}/delivery/`, DeliveryModel)
  }
}

