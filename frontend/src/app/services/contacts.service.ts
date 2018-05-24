import { Injectable } from '@angular/core';
import { Http, Response, Headers, URLSearchParams, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Contact } from '../models/contact';

@Injectable()
export class ContactsService {
  contactUrl = 'http://127.0.0.1:8000/contacts/';

  constructor(private http: Http) { }

  // Fetch all Companies
  getAllContacts(): Observable<Contact[]> {
    return this.http.get(this.contactUrl)
      .map(this.extractData)
        .catch(this.handleError);
  }

  // Delete Company
  deleteContactById(contactId: string): Observable<number> {
    let cpHeaders = new Headers({ 'Content-Type': 'application/json' });
    let options = new RequestOptions({ headers: cpHeaders });
    return this.http.delete(this.contactUrl + contactId + '/')
    .map(success => success.status)
    .catch(this.handleError);
  }

  private extractData(res: Response) {
    let body = res.json();
    return body;
  }

  private handleError (error: Response | any) {
    console.error(error.message || error);
    return Observable.throw(error.status);
  }

}



