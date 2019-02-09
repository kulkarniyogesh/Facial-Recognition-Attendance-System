import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { WorkingDaysData } from '../models/working_days.model';

@Injectable({
  providedIn: 'root'
})
export class AttendanceService {

  constructor(private http: HttpClient) {
  }

  getWorkingDays(): Observable<WorkingDaysData[]> {
    return this.http.get<WorkingDaysData[]>('https://fras-1.herokuapp.com/working-days/');
  }

}
