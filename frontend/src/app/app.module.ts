import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

// Components
import { AuthService } from './services/auth.service';
import { CompaniesService } from './services/companies.service';
import { ContactsService } from './services/contacts.service';

// Services
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ContactsComponent } from './components/contacts/contacts.component';
import { CompaniesComponent } from './components/companies/companies.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    ContactsComponent,
    CompaniesComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    RouterModule.forRoot([
      { path: 'login', component: LoginComponent },
      { path: 'dashboard', component: DashboardComponent },
      { path: 'contacts', component: ContactsComponent },
      { path: 'companies', component: CompaniesComponent },
      { path: '**', redirectTo: 'login', pathMatch: 'full' }
    ])
  ],
  providers: [AuthService, CompaniesService, ContactsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
