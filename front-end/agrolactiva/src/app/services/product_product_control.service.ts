import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { ProductControlModel } from '../models/product_product_controlModel';

@Injectable()
export class ProductControlService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getProductControles(): Observable<ProductControlModel[]> {
    return this.http.get<Array<ProductControlModel>>(this.apiUrl + '/product_product_control/');
  }

  getProductControlbyId(idProductControl: number): Observable<ProductControlModel> {
    return this.http.get<ProductControlModel>(this.apiUrl + '/product_product_control/' + idProductControl);
  }

  addProductControl(ProductControl:ProductControlModel): Observable<ProductControlModel> {
    return this.http.post<ProductControlModel>(`${this.apiUrl}/product_product_control/`, ProductControlModel)
  }
}

