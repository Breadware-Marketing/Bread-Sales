import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

import { Contact } from '../../models/contact';
import { ContactsService } from '../../services/contacts.service';

@Component({
  selector: 'app-contacts',
  templateUrl: './contacts.component.html',
  styleUrls: ['./contacts.component.css']
})
export class ContactsComponent implements OnInit {

  allContacts: Contact[];
  statusCode: number;
  requestProcessing = false;

  constructor(private contactService: ContactsService) { }

  ngOnInit(): void {
    this.getAllContacts();
  }

  // Fetch all Companies
  getAllContacts() {
    this.contactService.getAllContacts()
    .subscribe(
      data => this.allContacts = data,
      errorCode =>  this.statusCode = errorCode);
  }

  deleteContact(contactId: string) {
    this.preProcessConfigurations();
    this.contactService.deleteContactById(contactId)
      .subscribe(successCode => {
    // this.statusCode = successCode;
      // Expecting success code 204 from server
    this.statusCode = 204;
    this.getAllContacts();
    // this.backToCreateArticle();
  },
  errorCode => this.statusCode = errorCode);
 }

  // Perform preliminary processing configurations
  preProcessConfigurations() {
    this.statusCode = null;
    this.requestProcessing = true;
  }

}

