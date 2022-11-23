import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { ProductDispatchModel } from '../models/product_dispatchModel';

@Injectable()
export class ProductDispatchService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

  getProductDispatches(): Observable<ProductDispatchModel[]> {
    return this.http.get<Array<ProductDispatchModel>>(this.apiUrl + '/product_dispatch/');
  }

  getProductDispatchbyId(idProductDispatch: number): Observable<ProductDispatchModel> {
    return this.http.get<ProductDispatchModel>(this.apiUrl + '/product_dispatch/' + idProductDispatch);
  }

  addProductDispatch(ProductDispatch:ProductDispatchModel): Observable<ProductDispatchModel> {
    return this.http.post<ProductDispatchModel>(`${this.apiUrl}/product_dispatch/`, ProductDispatchModel)
  }
}

