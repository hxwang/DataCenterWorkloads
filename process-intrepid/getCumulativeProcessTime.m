
slot = 15*60;

pt = load('..\data\ANL-Intrepid-2009-1.swf\processTime.txt');
pt = ceil(pt /slot);

at = load('..\data\ANL-Intrepid-2009-1.swf\arrivalTime.txt');
at = ceil(at/slot);

cp = zeros(max(at)+max(pt)+2, 1);

%calculate cumulative workload
for i=1:size(at,1)
    start_time = at(i) + 1;
    end_time = at(i) + pt(i);
    cp(start_time:end_time) = cp(start_time:end_time) + 1;
end


figure1 = figure;
set(figure1,'units','normalized','outerposition',[0 0 1 1]);

axes1 = axes('Parent',figure1);
box(axes1,'on');
hold(axes1,'all');
set(axes1,'FontSize',30,'FontWeight','bold');


bar(cp)


ylabel('workload (15min)')
xlabel('time')

legend(axes1,'show','Location','NorthWest','FontSize',10,'FontWeight','bold');
legend('workload');
%save figure
set(gcf, 'PaperPosition', [0 0 13 7]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [13 7]); %Set the paper to have width 5 and height 5.

%path

saveas(gca, strcat(pwd,'\figs\cumulativeProcessingTime', '.eps'),'psc2') %Save figure 
saveas(gcf, strcat(pwd ,'\figs\cumulativeProcessingTime'), 'pdf') %Save figure 
saveas(gcf, strcat(pwd ,'\figs\cumulativeProcessingTime'), 'png') %Save figure 