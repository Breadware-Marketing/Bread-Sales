import { Injectable } from '@angular/core';
import { Http, Response, Headers, URLSearchParams, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Company } from '../models/company';

@Injectable()
export class CompaniesService {
  companyUrl = 'http://127.0.0.1:8000/company/';

  constructor(private http: Http) { }

  // Fetch all Companies
  getAllCompanies(): Observable<Company[]> {
    return this.http.get(this.companyUrl)
      .map(this.extractData)
        .catch(this.handleError);
  }

  // Create Company

  createCompany(company: Company): Observable<number> {
    const cpHeaders = new Headers({ 'Content-Type': 'application/json' });
    const options = new RequestOptions({ headers: cpHeaders });
    return this.http.post(this.companyUrl, company, options)
      .map(success => success.status)
      .catch(this.handleError);
  }

  // Update Company
  updateCompany(company: Company): Observable<number> {
    const cpHeaders = new Headers({ 'Content-Type': 'application/json' });
    const options = new RequestOptions ({ headers: cpHeaders });
    return this.http.put(this.companyUrl + '/' + company.id, company, options)
      .map(success => success.status)
      .catch(this.handleError);
  }

  // Delete Company
  deleteCompanyById(companyId: string): Observable<number> {
    const cpHeaders = new Headers({ 'Content-Type': 'application/json' });
    const options = new RequestOptions({ headers: cpHeaders });
    return this.http.delete(this.companyUrl + companyId + '/')
    .map(success => success.status)
    .catch(this.handleError);
  }

  private extractData(res: Response) {
    const body = res.json();
    return body;
  }

  private handleError (error: Response | any) {
    console.error(error.message || error);
    return Observable.throw(error.status);
  }

}
