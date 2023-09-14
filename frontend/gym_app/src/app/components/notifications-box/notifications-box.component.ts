import { Component } from '@angular/core';

@Component({
  selector: 'app-notifications-box',
  template: `
    <div class="box">
      <div class="notification-section">
        <div class="title">Notification</div>
        <div class="popup-notification">
          <div class="text">Pop-up Notification</div>
          <div class="toggle"><div class="ellipse"></div></div>
          <div class="icon-notif"><i class="fa-solid fa-bell"></i></div>
        </div>
      </div>
    </div>
  `,
  styles: [
    `
      .box {
        position: relative;
        width: 315px;
        height: 99px;
      }

      .box .notification-section {
        position: fixed;
        width: 315px;
        height: 99px;
        background-color: #ffffff;
        border-radius: 16px;
        box-shadow: 0px 10px 40px #1d161712;
        top: 0;
        left: 0;
      }

      .box .title {
        position: absolute;
        width: 87px;
        height: 24px;
        top: 20px;
        left: 20px;
      }

      .box .text-wrapper {
        position: absolute;
        font-family: 'Font Awesome 5 Free-Regular', Helvetica;
        font-weight: 400;
        color: #1d1517;
        font-size: 16px;
        letter-spacing: 0;
        line-height: 24px;
        white-space: nowrap;
        top: 0;
        left: 0;
      }

      .box .popup-notification {
        position: absolute;
        width: 280px;
        height: 20px;
        top: 59px;
        left: 20px;
      }

      .box .text {
        position: absolute;
        width: 113px;
        height: 18px;
        top: 1px;
        left: 30px;
      }

      .box .div {
        position: absolute;
        top: 0;
        left: 0;
        font-family: 'Font Awesome 5 Free-Regular', Helvetica;
        font-weight: 400;
        color: #7b6f72;
        font-size: 12px;
        letter-spacing: 0;
        line-height: 18px;
        white-space: nowrap;
      }

      .box .toggle {
        position: absolute;
        width: 36px;
        height: 18px;
        top: 1px;
        left: 244px;
        border-radius: 99px;
        background: linear-gradient(
          180deg,
          rgb(58, 106, 135) 0%,
          rgb(172.13, 172.13, 172.13) 100%
        );
      }

      .box .ellipse {
        position: relative;
        width: 12px;
        height: 12px;
        top: 3px;
        left: 21px;
        background-color: #ffffff;
        border-radius: 6px;
      }

      .box .icon-notif {
        position: absolute;
        width: 20px;
        height: 20px;
        top: 0;
        left: 0;
        background-size: 100% 100%;
      }
    `,
  ],
})
export class NotificationsBoxComponent {}
